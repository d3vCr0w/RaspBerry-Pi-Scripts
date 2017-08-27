#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pcd8544.lcd as lcd
import time, os, sys, thread
import psutil
import commands

if not os.geteuid() == 0:
    sys.exit('Script must be run as root')


def displayTemperatures():
    while True:
        try:
            cpuTemp = float(os.popen("cat /sys/class/thermal/thermal_zone0/temp").read())/1000
            gpuTemp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read().replace("temp=", "").replace("'", "")   
            #ip = os.popen("ip addr show eth0 | grep inet").read()
	    ip = commands.getoutput('hostname -I')
	    cpu_usage = str(psutil.cpu_percent())
            ram = psutil.phymem_usage()
	    ram_free = str(ram.free / 2**20)
	    
	    #Display Title
	    lcd.gotorc(0,0)
	    lcd.text("Raspberry Pi")
	    
	    #Display Time
	    lcd.gotorc(2,0)
    	    lcd.text("Time "+time.strftime("%I:%M:%S", time.localtime()))
            
	    #Display CPU Temp
	    cpu_temperature_display = "{0:0.1f}".format(cpuTemp)
            lcd.gotorc(3,0)
	    #lcd.text("")
            lcd.text("CPU {}C {}%".format(cpu_temperature_display, cpu_usage))
            
	    #Display GPU Temp
            lcd.gotorc(4,0)
	    #lcd.text("            ")
            lcd.text("GPU {}".format(gpuTemp))

	    #*****************Second Page**********************
	    #time.sleep(1)

	    #Display Time
            #lcd.gotorc(2,0)
            #lcd.text("Time "+time.strftime("%I:%M:%S", time.localtime()))

            #Display Free RAM
	    lcd.gotorc(5,0)
	    lcd.text("RAM "+ram_free+"MB Free")
	    #Display IP
	    #lcd.gotorc(4,0)
	    #lcd.text(ip)	  

	    time.sleep(1)

	    #lcd.cls()
        except KeyboardInterrupt:
            sys.exit(0)

def displayTime():
    #Display Time
    lcd.gotorc(2,0)
    lcd.text(time.strftime("%I:%M:%S", time.localtime()))
    time.sleep(0.25)
    lcd.cls()

try:
    lcd.init()
    lcd.cls()  
    displayTemperatures()
except KeyboardInterrupt:
    pass
finally:
    lcd.cls()
