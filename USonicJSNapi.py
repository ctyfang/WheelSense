#Libraries
import RPi.GPIO as GPIO
import time, threading
import numpy as np

class USSensor(threading.Thread):
	TRIG = 27                                  #Associate pin 15 to TRIG
	ECHO = 17                                  #Associate pin 14 to Echo
	distance = 0
	isInit = False
	def __init__(self, TRIG_PIN, ECHO_PIN):
		threading.Thread.__init__(self)

		#GPIO Mode (BOARD / BCM)
		GPIO.setmode(GPIO.BCM)

		print "Distance measurement in progress"
		self.TRIG = TRIG_PIN
		self.ECHO = ECHO_PIN
		GPIO.setup(self.TRIG,GPIO.OUT)                  #Set pin as GPIO out
		GPIO.setup(self.ECHO,GPIO.IN)                   #Set pin as GPIO in

	
	def run(self):
		self.initialize()
		while True:
		 	self.getDistance()
			time.sleep(0.01)
	
	def initialize(self):

	    GPIO.output(self.TRIG, False)                 #Set TRIG as LOW
	    print "Waiting For Sensor To Settle"
	    time.sleep(2)                            #Delay of 2 seconds
	    self.isInit = True

	def getDistance(self):
		GPIO.output(self.TRIG, True)                  #Set TRIG as HIGH
		time.sleep(0.00001)                      #Delay of 0.00001 seconds
		GPIO.output(self.TRIG, False)                 #Set TRIG as LOW

		while GPIO.input(self.ECHO)==0:               #Check if Echo is LOW
			pulse_start = time.time()              #Time of the last  LOW pulse

		while GPIO.input(self.ECHO)==1:               #Check whether Echo is HIGH
			pulse_end = time.time()                #Time of the last HIGH pulse 

		distance = np.round((pulse_end-pulse_start)*1750, 2)            #Round to two decimal points

		if distance > 20 and distance < 800:     #Is distance within range
			#print "Distance:",distance - 0.5,"cm"  #Distance with calibration
			self.distance = distance
 

# if __name__ == '__main__':

#     #
# 	_thread = USSensor()
# 	_thread.start()     
