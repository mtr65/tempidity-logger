#!/usr/bin/python3

#from subprocess import Popen, PIPE
from time import sleep
#from datetime import datetime
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN    = 4

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

# lcd.message = "\x00"
# wipe LCD screen before we start
# lcd.backlight = true

lcd.clear()

# before we start the main loop - detect active network device and ip address

#leep(2)
#interface = find_interface()
#ip_address = parse_ip()

while True:
    # lcd.clear()
    # Read DHT22 module data
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    tempfahr = (temperature * 1.8 ) + 32

    # date and time
    # lcd_line_1 = datetime.now().strftime('%b %d  %H:%M:%S\n')
    # lcd.message = datetime.now().strftime('%b %d  %H:%M:%S\n')
    # sleep(10)
    # lcd.clear()
    ##lcd_line_1 = ('Temp: %d\x00C ' % temperature)
    ##lcd_line_2 = ('%d\x00F\n' % tempfahr)
    lcd_line_1 = ('Temp: %d\x00c %d\x00F\n' %(temperature, tempfahr))
    lcd_line_2 = ('Humidity: %d%%' % humidity)
    # lcd_line_1 = ('Temp: {0:0.1f}C/{1:0.1f}F\n'.format(temperature, tempfahr)

    #lcd_line_3 = ('Humidity: %d%%' % humidity)
    # lcd_line_2 = ('Humidity: {0}%%'.format(humidity)

    # combine both lines into one update to the display
    lcd.message = lcd_line_1 + lcd_line_2 # + lcd_line_3

    # scroll_msg = lcd_line_1 + lcd_line_2 + lcd_line_3
    # scroll_msg = "Yo Dude!"
    # lcd.message = scroll_msg
    # Scroll message to the left
    # for i in range(len(scroll_msg)):
       # sleep(0.5)
       # lcd.move_left()
    # lcd.clear()

    sleep(10)
