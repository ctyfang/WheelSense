from USonicJSNapi import USSensor
from dataTransferServer import *




#This class initiates all sensor acquisition software threads, and polls them for data at 
#a specified rate.
class mainSensorAcquistion():

	def __init__(self):
		self.initWheelSensors()
		self.initUltraSonicSensors()
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

		self.USonicThreadDown = USSensor()
		self.USonicThreadDown.start()

	# TODO Get this working
	# https: // github.com / MomsFriendlyRobotCompany / mpu9250 / blob / master / mpu9250 / mpu9250.py
	def initOrientationSensor(self):
		# write this

	# TODO Get this working
	# https://pypi.org/project/mpu6050-raspberrypi/
	def initIMUSensor(self):
		# write this

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



