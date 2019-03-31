from USonicJSNapi import USSensor
from dataTransferServer import *
from mpu6050 import mpu6050
from IMUThread import IMUSensor
from OrientationThread import OrientationSensor
from WheelIMUThread import WheelIMUThread
import sched,time

#This class initiates all sensor acquisition software threads, and polls them for data at 
#a specified rate.

	
class mainSensorAcquisition():

	def __init__(self):
		self.initWheelSensors()
		self.initUltraSonicSensors()
		self.initOrientationSensor()
		#self.initIMUSensor()
		# self.initCameraSensor()
		
		self.value = 0
		print("Threads have been started")
		self.poll()

	# TODO Set GPIO pins for Ultrasonic sensors
	def initUltraSonicSensors(self):
		self.USonicThreadForward = USSensor(27, 17)
		self.USonicThreadForward.start()

		#self.USonicThreadDown = USSensor()
		#self.USonicThreadDown.start()

	def initOrientationSensor(self):
		self.OrientationThread = OrientationSensor()
		self.OrientationThread.start()
		
	def initIMUSensor(self):
		self.IMUThread = IMUSensor()
		self.IMUThread.start()

	# TODO Check if this works
	def initWheelSensors(self):
		# Connect to left
		self.leftWheelThread = WheelIMUThread()
		self.leftWheelThread.start()

		# Connect to right - TODO Change UUID for second wheel module

	def poll(self):
		# Collect data from all sensors
		while(True):
			# Create packet
			dataPacket = {}
			#print("START")
			#print(time.time())
			dataPacket["accel"] = self.OrientationThread.MPU.accel
			dataPacket["gyro"] = self.OrientationThread.MPU.gyro
			dataPacket["yaw"] = self.OrientationThread.Fusion.heading
			dataPacket["pitch"] = self.OrientationThread.Fusion.pitch
			dataPacket["roll"] = self.OrientationThread.Fusion.roll
			dataPacket["front_dist"] = self.USonicThreadForward.distance
			dataPacket["left_wheel"] = self.leftWheelThread.data
			
			#self.testSched.enter(0.01, 1, self.poll, ())
			#self.testSched.run()
			# Format into protobuf
			#print("END")
			#print(time.time())
			print(self.value)
			self.value += 1
			time.sleep(0.001)
		# Transmit to laptop
		
	
if __name__ == '__main__':
	_mainServer = mainSensorAcquisition()



