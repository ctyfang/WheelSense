import socket
import os, imp, struct, threading, csv
from bluetooth import *
import datetime
import bluetooth, signal, sys
from enum import Enum
import time

dir_path = os.path.dirname(os.path.realpath(__file__))
print("Base path=" + dir_path)

imuMsgPath = dir_path + "\\release\\imumsg_pb2.py"
imuMsg = imp.load_source("imumsg_pb2", imuMsgPath)

class WheelIMUThread(threading.Thread):
    connected = False
    # If true choose blueTooth connection
    blueTooth = False
    _maxClients = 1
    _numClients = 0
    _serverRunning = True

    def __init__(self):
        threading.Thread.__init__(self)

    def startServerBlueTooth(self):

        while self._serverRunning:

            if self._numClients < self._maxClients:

                self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                self.sock.connect(("98:D3:51:FD:AD:F5", 1))
                print("Connected to Socket")

                self._numClients = self._numClients + 1
                _thread = IMUMsgThread(self.sock, self)
                _thread.start()

    def run(self):
        self.startServerBlueTooth()

    # Ran after connection is made
    def controlLoop(self):
        _thread = IMUMsgThread(self.clientsocket, self)
        _thread.start()

    @property
    def numClients(self):
        return self._numClients

    def removeClient(self):
        ##For now just lower number clients connected
        self._numClients = self._numClients - 1


    def shutDown(self):
        self.sock.close()
        self._serverRunning = False
        sys.exit(0)

    def receive(self, MSGLEN):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.clientsocket.recv(1)
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return ''.join(chunks)


class IMUMsgThread(threading.Thread):
    # Thread is running
    _running = True
    msgsRecieved = 0

    def __init__(self, clientSocket, parentServer):
        threading.Thread.__init__(self)
        self.clientsocket = clientSocket
        self._parentServer = parentServer

    # self.clientsocket.setblocking(0)


    def run(self):
        #self.csvFile = open(dir_path + "\\imu_data\\" + DATA_PATH, 'wb')
        #self.CSVData = csv.writer(self.csvFile)

        while True:
            try:
                self.getIMUMsg()
                self.msgsRecieved = self.msgsRecieved + 1
                print("Success! Received message " % self.msgsRecieved)
            except:
                print("ERROR getting message")
                pass

        # time.sleep(0.050)
        #self.csvFile.close()

    def getIMUMsg(self):
        dataSizeArray = self.receive(4)

        # dataSizeArray = dataSizeArray[0:1]
        dataSize = struct.unpack("<L", dataSizeArray)[0]
        if (dataSize < 100):

            data = self.receive(dataSize)

            # Get incoming data.
            _imuMsg = imuMsg.IMUInfo()
            _imuMsg.ParseFromString(data)

            # Do things in real-time HERE ...

            # Log data to a CSV
            #self.CSVData.writerow(
            #    [datetime.datetime.now().strftime("%H:%M:%S.%f"), _imuMsg.acc_x, _imuMsg.acc_y, _imuMsg.acc_z,
            #     _imuMsg.angular_x, _imuMsg.angular_y, _imuMsg.angular_z])

            return _imuMsg

        else:
            print("Invalid Size of %i \n" % dataSize)
            return False

    ###
    def receive(self, MSGLEN):
        # data = self.clientsocket.recv(MSGLEN)
        # return data
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            # print("Waiting for msg")
            chunk = self.clientsocket.recv(1)
            # self.clientsocket.readsock(1)
            # print str(chunk)
            if chunk == '':
                # raise RuntimeError("socket connection broken")
                print("socket connection broken shutting down this thread")
                self.shutDown()
                return 0

            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return ''.join(chunks)

    def shutDown(self):
        self.clientsocket.close()
        #self.csvFile.close()
        self._running = False
        self._parentServer.removeClient()



if __name__ == "__main__":
    _msgServerThread = WheelIMUThread()
    _msgServerThread.start()

