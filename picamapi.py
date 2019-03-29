from picamera import PiCamera
from time import sleep
import threading
import numpy as np
from PIL import Image

# It is also important to note that when outputting to unencoded formats, 
# the camera rounds the requested resolution. The horizontal resolution is 
# rounded up to the nearest multiple of 32 pixels, while the vertical resolution 
# is rounded up to the nearest multiple of 16 pixels. For example, if the 
# requested resolution is 100x100, the capture will actually contain 128x112 
#  worth of data, but pixels beyond 100x100 will be uninitialized.
camera = PiCamera()
def main():
	

	camera.start_preview()
	print("taking pics")
	
	sleep(10)
	camera.capture('/home/pi/Desktop/image.jpg')
	camera.stop_preview()


class piCam(threading.Thread):
	
	camera = PiCamera()
	def __init__(self):
		threading.Thread.__init__(self)
		

	def getImg(self):
		output = np.empty((112 * 128 * 3,), dtype=np.uint8)
		self.camera.capture(output, 'rgb')
		output = output.reshape((112, 128, 3))
		output = output[:100, :100, :]
		return output

	def run(self):
		
		self.camera.resolution = (100, 100)
		self.camera.framerate = 24
		print("Starting run")
		sleep(2)
		self.displayImage(self.getImg())	

	def displayImage(self, imgArray):
		# w, h = 512, 512
		# data = np.zeros((h, w, 3), dtype=np.uint8)
		# data[256, 256] = [255, 0, 0]
		img = Image.fromarray(imgArray, 'RGB')
		img.save('/home/pi/testimage.jpg')
		img.show()

	

if __name__=="__main__":
	
	#_thread = piCam()
	#_thread.start()	
	#_thread.displayImage(_thread.getImg())	
	main()