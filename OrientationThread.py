#Libraries
import time, threading
from mpu9250 import mpu9250
from fusion import Fusion
import time
import datetime

def timediff(end, start):
	return ((end-start).microseconds)*1000000
	
class OrientationSensor(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.Fusion = Fusion(timediff)
		self.MPU = mpu9250()
	
	def run(self):
		while(True):
			print(time.time())
			self.Fusion.update(self.MPU.accel, self.MPU.gyro, self.MPU.mag, datetime.datetime.now())
			#self.Fusion.heading/pitch/roll for the data
			print(time.time())
			time.sleep(0.01)
