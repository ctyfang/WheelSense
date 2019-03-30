from USonicJSNapi import USSensor
from dataTransferServer import *
from mpu6050 import mpu6050
from IMUThread import IMUSensor
from OrientationThread import OrientationSensor


#This class initiates all sensor acquisition software threads, and polls them for data at 
#a specified rate.

	
class mainSensorAcquistion():

	def __init__(self):
		#self.initWheelSensors()
		#self.initUltraSonicSensors()
		self.initOrientationSensor()
		self.initIMUSensor()
		# self.initCameraSensor()

		print("Threads have been started")

		#
		pass

	# TODO Set GPIO pins for Ultrasonic sensors
	def initUltraSonicSensors(self):
		self.USonicThreadForward = USSensor()
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
		self._leftWheelThread = msgServer(dataTransferMode.BLUETOOTH)
		self._leftWheelThread.start()

		# Connect to right - TODO Change UUID for second wheel module
		self._rightWheelThread = msgServer(dataTransferMode.BLUETOOTH)
		self._rightWheelThread.start()

if __name__ == '__main__':
	_mainServer = mainSensorAcquistion()



