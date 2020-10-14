#!/usr/bin/python3
#
# Source File: tempidity-logger_betaV1.0.2.py
#
# Description: A program to interface a DHT22 temperature & humidity sensor module with a
#              Raspberry Pi via GPIO pins in order to log sensor data to a CSV logfile
#              and display the readings in a terminal window.
#
# Copyright © 2020 Matt Robbins [mtr@mattrobbins.net]
#
# Last updated October 13, 2020.
#

import os
import sys
import time
import datetime
import Adafruit_DHT
from pathlib import Path

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

CEND = '\33[0m'
CBLUEBG = '\33[44m'
CYELLOWBG = '\33[43m'
CRED2 = '\33[91m'

try:
    os.system('clear')
    print("\n\n  \33[7m Reading temperature and humidity data from  \33[92m Sensor #1 \33[0m\n\n")

    while True:
        logFile = open(Path.home() / Path('log/') / 'tempidity_data.csv', "a+")
        if os.path.getsize(Path.home() / Path('log/') / 'tempidity_data.csv') == 0:
            logFile.write("Date,Time,Temperature,Humidity\r\n")

        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        now = datetime.datetime.now()
        tempfahr = (temperature * 1.8) + 32

        if humidity is not None and temperature is not None:
            logFile = open(Path.home() / Path('log/') / 'tempidity_data.csv', "a+")
            logFile.write('{0},{1},{2:0.1f},{3:0.1f}\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M:%S'), temperature, humidity))
            print(now.strftime(CRED2 + " %m-%d-%Y %H:%M:%S" + CEND), CBLUEBG + " Temp: {0:0.1f}\u00B0C/{1:0.1f}\u00B0F \33[0m " "\33[42m Humidity: {2:0.1f}% \33[0m".format(temperature, tempfahr, humidity))
            logFile.close()

        else:
            print("Failed to retrieve data from sensor")

        time.sleep(60)

except KeyboardInterrupt:
    print("\n\n\t****  Exiting program tempidity-logger ****\n\n")
    sys.exit()
