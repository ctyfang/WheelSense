import socket
import os, imp, struct, threading, csv
from bluetooth import *
import datetime
import bluetooth, signal, sys
from enum import Enum
import time
import numpy as np

DATA_PATH = "test.csv"
COLLECTION_TIME = 2

dir_path = os.path.dirname(os.path.realpath(__file__))
print("Base path=" + dir_path)

imuMsgPath = dir_path+ "/release/imumsg_pb2.py"
imuMsg = imp.load_source("imumsg_pb2",imuMsgPath)

#Class defines mode of data transfer
class dataTransferMode(Enum):
	TCP = 1
	BLUETOOTH = 2

class WheelIMUThread(threading.Thread):
	connected = False
	#If true choose blueTooth connection
	blueTooth = False
	_maxClients = 1
	_numClients = 0
	_serverRunning = True
	
	def __init__(self):
		threading.Thread.__init__(self)

		print("Binding to port")
		self.transferMode = dataTransferMode(2)

	def run(self):
		#self.startServer()
		if(self.transferMode == dataTransferMode.TCP):
			self.startTCPServer()
		elif(self.transferMode == dataTransferMode.BLUETOOTH):
			self.startServerBlueTooth()

	
	def startTCPServer(self):
			print("Binding to port")
			#create an INET, STREAMing socket
			self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			#bind the socket to a public host,
			# and a well-known port
			print("Binding to port")
			self.serversocket.bind((HOST, PORT))
			print("Succesfully connected to a client")

			#self.controlLoop()

			#while True:
			
	#Ran after connection is made
	def controlLoop(self):
		_thread = IMUMsgThread(self.clientsocket,self)
		_thread.start()		


	@property
	def numClients(self):
		return self._numClients

	def removeClient(self):
		##For now just lower number clients connected
		self._numClients = self._numClients - 1
	
	def startServerBlueTooth(self):

		while self._serverRunning:
			
			if self._numClients < self._maxClients:

				sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
				sock.connect(("98:D3:51:FD:AD:F5",1))
				print("Connected to Socket")

				self._numClients = self._numClients + 1
				_thread = IMUMsgThread(sock,self)
				_thread.start()

	def shutDown(self):

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
	#Thread is running
	_running = True
	msgsRecieved=0
	def __init__(self, clientSocket, parentServer):
		threading.Thread.__init__(self)
		self.clientsocket = clientSocket
		self._parentServer = parentServer
		#self.clientsocket.setblocking(0)
		

	def run(self):

		while (True):
			print("Pre-fetch")
			print(time.time())
			try:
				self.data = self.getIMUMsg()
				self.msgsRecieved = self.msgsRecieved + 1
				#print("Message number %i" %self.msgsRecieved )
			except:
				#print("ERROR getting message")
				pass				
			print("Post-fetch")
			print(time.time())

			#time.sleep(0.050)
			#print("Seconds passed = " + str((currentTime-startTime).seconds))
		#self.csvFile.close()



	def getIMUMsg(self):
		dataSizeArray = self.receive(4)
		dataSize = np.ndarray((1,), '<L', dataSizeArray, 0, (4,))
	 	if(dataSize < 100):

			data = self.receive(dataSize)

			# Get incoming data.
			_imuMsg = imuMsg.IMUInfo()
			_imuMsg.ParseFromString(data)
			# Do things in real-time HERE ...

			# Log data to a CSV
			#self.CSVData.writerow([datetime.datetime.now().strftime("%H:%M:%S.%f"), _imuMsg.acc_x,_imuMsg.acc_y,_imuMsg.acc_z,_imuMsg.angular_x,_imuMsg.angular_y,_imuMsg.angular_z])

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
			chunks.append(self.clientsocket.recv(1))
			bytes_recd = bytes_recd +  1
		return ''.join(chunks)	

	def shutDown(self):
		self.clientsocket.close()
		self.csvFile.close()
		self._running = False
		self._parentServer.removeClient()


def connect():
	sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	sock.connect(("98:D3:51:FD:AD:F5",1))
	print("Connected to Socket")
	bytes_recd = 0
	MSGLEN =1
	while bytes_recd < MSGLEN:
		#chunk = sock.recv(1)
		sock.send("HelloWorld")
		#print str(chunk)
		bytes_recd = bytes_recd + 1
	input("Press enter to close")

	sock.close()



	# s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

	# target_name = "HC-05-LEFT"
	# target_address = None

	# nearby_devices = bluetooth.discover_devices()

	# for bdaddr in nearby_devices:
	# 	name = bluetooth.lookup_name( bdaddr )
	# 	print(name)
	# 	if target_name == name:
	# 		target_address = bdaddr
	# 		break

	# if target_address is not None:
	# 	print "found target bluetooth device with address ", target_address


	# else:
	# 	print "could not find target bluetooth device nearby"

	# sock.close()

#if __name__=="__main__":
#	
#	print("Binding to port")
#	_msgServerThread = msgServer(dataTransferMode.BLUETOOTH)
#	_msgServerThread.start()

