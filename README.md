# tempidity-logger

Python 3 code for display and logging of temperature and humidity data from a DHT22 digital sensor module.

The main goal for this project is for me to start learning how to program with Python 3 and to develop
the software needed to build various Raspberry Pi based projects like a weather station.

A secondary goal of this project is to learn how to use GitHub for version control.

DESCRIPTION: A Python 3 program for connecting a DHT22 temperature & humidity sensor module to a
             Raspberry Pi via the GPIO interface in order to log sensor data readings to a CSV log file
             and display the readings in a terminal window.

For this project I am using a Raspberry Pi Model 3 A+ with a DHT22 digital 
temperature/humidity sensor module connected to the RPi GPIO pin 4.

I started the project by following the guide located at:

https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/

This got me up and running but I decided to modify the code to simplify the file paths for logging and change
the display formatting while adding a conversion to Fahrenheit for display(not logged to file). After my changes I went
back over it all to clean up some spots to make it easier to follow while adding a more logical main loop format.

Below is the pinout description from the guide above for connectng the DHT22 module followed by a link showing the wiring
diagram for using a breadboard circuit.

   - Place a 10k resistor between Pin 1 and Pin 2 of the DHT22
   - Wire Pin 1 of the DHT22 to Physical Pin 1 (3v3) on the Pi
   - Wire Pin 2 of the DHT22 to Physical Pin 7 (GPIO4) on the Pi
   - Wire Pin 4 of the DHT22 to Physical Pin 6 (GND) on the Pi


https://pi.lbbcdn.com/wp-content/uploads/2019/05/Raspberry-Pi-Humidity-Sensor-DHT22-Wiring-Schematic.png



***********************************************************************************

The current version of this program is tempidity-logger_betaV1.0.4.py in the /src directory.

Read the CHANGELOG.md file for update info.

UPDATED: July 31, 2021

...
