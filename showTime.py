import time

def showTime():
    print(time.strftime("%I:%M:%S", time.localtime()))

try:
    showTime()
    sleep(1)
except KeyboardInterrupt:
    print("")
