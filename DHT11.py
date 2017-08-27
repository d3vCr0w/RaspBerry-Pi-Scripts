#!/usr/bin/python
import sys
import Adafruit_DHT
import time
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

def getMeasurements():
    while True:
	try:
            humidity, temperature = Adafruit_DHT.read_retry(11, 4)
	    ser.write('Temp: {0:0.1f}C  Humidity: {1:0.1f}%'.format(temperature, humidity))
	    time.sleep(2)
	except KeyboardInterrupt:
	    sys.exit(0)


def displayMeasurements():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
	ser.write('Temp: {0:0.1f}C  Humidity: {1:0.1f}%'.format(temperature, humidity))
	time.sleep(2)


def main():
    #print "Select an option"
    #print "1 Show Measurements here"
    #print "2 Show Measurements in LCD Display"
    try:
        #option=int(raw_input("=>"))
        option=int(sys.argv[1])
    except ValueError:
        print "Not a number"

    if option==1:
        #print "Get Measurements"
        getMeasurements()
    elif  option==2:
        #print "Display Measurements in LCD"
        displayMeasurements()        


main()
