#!/usr/bin/python3
#
# Source File: tempidity-logger_betaV1.0.4.py
#
# DESCRIPTION: A Python 3 program for connecting a DHT22 temperature & humidity sensor module to a
#              Raspberry Pi via the GPIO interface in order to log sensor data readings to a CSV log file
#              and display the readings in a terminal window.
#
# Copyright © 2020 Matt Robbins [mtr@mattrobbins.net]
#
# Last updated October 23,2020.
#

import os, sys, time, datetime
import Adafruit_DHT
from pathlib import Path
from gpiozero import LED
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

led = LED(16)

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

# compatible with all versions of RPI as of Jan. 2019
# v1 - v3B+
lcd_rs = digitalio.DigitalInOut(board.D22)
lcd_en = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d6 = digitalio.DigitalInOut(board.D23)
lcd_d7 = digitalio.DigitalInOut(board.D18)
lcd_backlight = digitalio.DigitalInOut(board.D5)

# Initialise the lcd class
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                      lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

# Create applicable byte codes for a standard pre-programmed character
# on a HD44780 LCD controller
checkmark = bytes([0x0, 0x18, 0x18, 0x18, 0x0, 0x0, 0x0, 0x0])

# Store byte code in LCD character memory 0
lcd.create_char(0, checkmark)

lcd.clear()

CEND = '\33[0m'
CBLUEBG = '\33[44m'
CYELLOWBG = '\33[43m'
CRED2 = '\33[91m'

try:
    os.system('clear')
    print("\n\n  \33[7m Reading temperature and humidity data from \33[92m  Sensor #1 \33[0m\n\n")

    while True:
        logFile = open(Path.home() / Path('log/') / 'tempidity_data.csv', "a+")
        if os.path.getsize(Path.home() / Path('log/') / 'tempidity_data.csv') == 0:
            logFile.write("Date,Time,Temperature,Humidity\r\n")

        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        now = datetime.datetime.now()
        tempfahr = (temperature * 1.8) + 32

        if humidity is not None and temperature is not None:
            logFile = open(Path.home() / Path('log/') / 'tempidity_data.csv', "a+")
            logFile.write('{0},{1},{2:0.1f},{3:0.1f}\r\n'.format(time.strftime('%m/%d/%y'),
                time.strftime('%H:%M:%S'), temperature, humidity))
            print(now.strftime(CRED2 + " %m-%d-%Y %H:%M:%S" + CEND),
                CBLUEBG + " Temp: {0:0.1f}\u00B0C/{1:0.1f}\u00B0F \33[0m " "\33[42m Humidity: {2:0.1f}% \33[0m".format
                (temperature, tempfahr, humidity))
            logFile.close()

            lcd_line_1 = ('Temp: %d\x00C %d\x00F\n' % (temperature, tempfahr))
            lcd_line_2 = ('Humidity: %d%%' % humidity)

            lcd.message = lcd_line_1 + lcd_line_2

            led.blink(1, 9)

        else:
            print("Failed to retrieve data from sensor")

        time.sleep(60)

except KeyboardInterrupt:
    print("\n\n\t*******  ENDING PROGRAM EXECUTION *******\n\n")
    sys.exit()
