import os
import time
import sys
import Adafruit_DHT
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    try:
        cpuTemp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").read()
        gpuTemp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        ser.write('Temp: {0:0.1f}C  Humidity: {1:0.1f}%'.format(temperature, humidity))
        time.sleep(1)
        ser.write("CPU temp={0:0.1f}'C".format(float(cpuTemp)/1000))
        ser.write(" GPU {} ".format(gpuTemp))
        time.sleep(1)  
    except KeyboardInterrupt:
        sys.exit(0)
