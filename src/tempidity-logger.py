#!/usr/bin/python3
# Source File name: tempidity_logger_v5.py
# Copyright © 2020 Matt Robbins [mtr@mattrobbins.net]
# 
#

import os
import time
import datetime
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

try:
    fo = open("/home/wisdom/Code/Python/tempidity_data.csv", "a+")
    if os.stat("/home/wisdom/Code/Python/tempidity_data.csv").st_size == 0:
        fo.write("Date,Time,Temperature,Humidity\r\n")

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
        print(now.strftime("%m-%d-%Y %H:%M:%S"),"Temp: {0:0.1f}\u00B0C {1:0.1f}\u00B0F Humidity: {2:0.1f}%".format(temperature, tempfahr, humidity))
        fo.close()
    else:
        print ("Failed to retrieve data from sensor")

    time.sleep(30)
