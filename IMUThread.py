#Libraries
import time, threading
from mpu6050 import mpu6050

class IMUSensor(threading.Thread):

	isInit = False
	def __init__(self):
		threading.Thread.__init__(self)
	
	def run(self):
		self.initialize()
		while(True):
			self.updateMeasurements()
	
	def initialize(self):
		self.IMU = mpu6050(0x68)

	def updateMeasurements(self):
		accel_data = self.IMU.get_accel_data()
		gyro_data = self.IMU.get_gyro_data()
		self.data = {'ax':accel_data['x'], 'ay':accel_data['y'], 'az':accel_data['z'], 'gx':gyro_data['x'], 'gy':gyro_data['y'], 'gz':gyro_data['z']}
		#print(self.IMU.data)

# if __name__ == '__main__':

#     #
# 	_thread = USSensor()
# 	_thread.start()     
