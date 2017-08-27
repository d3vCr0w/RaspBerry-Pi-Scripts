import time

def showTime():
	while True:
		print time.strftime("%I:%M:%S", time.localtime())
		time.sleep(1)

showTime()