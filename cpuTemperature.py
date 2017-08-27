import os
import time
import sys
import traceback
import serial

#ser = serial.Serial('/dev/ttyACM0', 9600)

def getTemperatures():
    while True:
        try:
	    print "CPU and GPU Temperature"
	    print "***********************"
	    cpuTemp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").read()
	    gpuTemp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
	    print "CPU temp={0:0.1f}'C".format(float(cpuTemp)/1000)
	    print "GPU {}".format(gpuTemp)
            time.sleep(0.25)
	    os.system("clear")
        except KeyboardInterrupt:
	    print " Exit"
            sys.exit(0)


def displayTemperatures():
    while True:
        try:
            cpuTemp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").read()
            gpuTemp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
            ser.write("CPU temp={0:0.1f}'C".format(float(cpuTemp)/1000))
            ser.write(" GPU {} ".format(gpuTemp))
            time.sleep(1)
        except KeyboardInterrupt:
            sys.exit(0)

def main():
    #print "Select an option"
    #print "1 Show temperatures here"
    #print "2 Show temperatures in LCD Display"
    try:
        #option=int(raw_input("=>"))
        option=int(sys.argv[1])
    except ValueError:
        print "Not a number"

    if option==1:
        #print "Get Temperatures"
        getTemperatures()
    elif  option==2:
        #print "Display in LCD"
        displayTemperatures()        


main()
