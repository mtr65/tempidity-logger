#!/usr/bin/python3
# Source File name: tempidity_logger_v6.1.py
# Copyright © 2020 Matt Robbins [mtr@mattrobbins.net]
#
# Last updated June 8, 2020

import os
import time
import datetime
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN    = 4

CEND       = '\33[0m'
CBLUEBG    = '\33[44m'
CYELLOWBG  = '\33[43m'
CRED2      = '\33[91m'

try:
    fo = open("/home/wisdom/Code/Python/tempidity_data.csv", "a+")
    if os.stat("/home/wisdom/Code/Python/tempidity_data.csv").st_size == 0:
        fo.write("Date,Time,Temperature,Humidity\r\n")

    os.system('clear')    
    print("\n\n  \33[7m Reading temperature and humidity data from  \33[92m Sensor #1 \33[0m\n\n")    

except:
    pass

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    now = datetime.datetime.now()
    tempfahr = (temperature * 1.8 ) + 32
                                                    
    if humidity is not None and temperature is not None:
        fo = open("/home/wisdom/Code/Python/tempidity_data.csv", "a+")
        fo.write('{0},{1},{2:0.1f},{3:0.1f}\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M:%S'), temperature, humidity))
#         print (now.strftime("%Y-%m-%d %H:%M:%S"))
        print(now.strftime(CRED2 + " %m-%d-%Y %H:%M:%S" + CEND), CBLUEBG + " Temp: {0:0.1f}\u00B0C/{1:0.1f}\u00B0F \33[0m " "\33[42m Humidity: {2:0.1f}% \33[0m".format(temperature, tempfahr, humidity))
        fo.close()
    else:
        print ("Failed to retrieve data from sensor")

    time.sleep(60)
