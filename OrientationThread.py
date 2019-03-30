#Libraries
import time, threading
from mpu9250 import mpu9250
from fusion import Fusion
import time
import datetime

def timediff(end, start):
	delta = end-start
	return (delta.microseconds)*1000000
	
class OrientationSensor(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.Fusion = Fusion(timediff)
		self.MPU = mpu9250()
		
		mag_data = self.MPU.mag
	
	def run(self):
		while(True):
			accel_data = self.MPU.accel
			gyro_data = self.MPU.gyro
			mag_data = self.MPU.mag
			self.Fusion.update(accel_data, gyro_data, mag_data, datetime.datetime.now())
			#self.Fusion.heading/pitch/roll for the data



# if __name__ == '__main__':

#     #
# 	_thread = USSensor()
# 	_thread.start()     
