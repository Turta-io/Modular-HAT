#!/usr/bin/env python3

#This sample demonstrates digital port read and write.
#Install Modular HAT library with "pip3 install turta-modularhat"

#Raspberry Pi Configuration
# - You should enable SPI and I2C from the Raspberry Pi's configuration.
# To do so, type 'sudo raspi-config' to the terminal, then go to 'Interfacing Options' and enable both SPI and I2C.


from time import sleep
from turta_modularhat import Turta_Digital

#Initialize
#Set left digital port as output, right digital port as input
digital = Turta_Digital.DigitalPort(False, False, True, True)

try:
    while True:
        #Turn pin 1 on
        digital.write(1, True)
        print("Pin 1 is set to high.")

        #Wait
        sleep(1.0)

        #Turn pin 1 off
        digital.write(1, False)
        print("Pin 1 is set to low.")

        #Wait
        sleep(1.0)

        #Toggle pin 2
        #Toggling inverts the pin state
        digital.toggle(2)
        print("Pin 2 is inverted to " + ("high." if digital.read(2) else "low."))

        #Wait
        sleep(1.0)

        #Read pin 3 and 4
        pin3 = digital.read(3)
        pin4 = digital.read(4)

        #Print pin 3 and 4 states
        print("Pin 3 state is " + ("high." if pin3 else "low."))
        print("Pin 4 state is " + ("high." if pin4 else "low."))

        #Wait
        sleep(1.0)

#Exit on CTRL+C
except KeyboardInterrupt:
    print('Bye.')
