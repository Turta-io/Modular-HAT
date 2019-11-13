#!/usr/bin/env python3

#This sample demonstrates measuring analog inputs from modules.
#Install Modular HAT library with "pip3 install turta-modularhat"

#Raspberry Pi Configuration
# - You should enable SPI and I2C from the Raspberry Pi's configuration.
# To do so, type 'sudo raspi-config' to the terminal, then go to 'Interfacing Options' and enable both SPI and I2C.

from time import sleep
from turta_protohat import Turta_Analog

#Initialize
analog = Turta_Analog.ADC()

try:
    while True:
        #Read analog input on module 1
        a1 = analog.read(Turta_Analog.CH.MODULE_1)

        #Read analog input on module 2
        a2 = analog.read(Turta_Analog.CH.MODULE_2)

        #Read board temperature
        board_temp_c = analog.read_temperature()
        board_temp_f = analog.read_temperature(True)

        #Print the readings
        print("Module 1 Analog.: " + str(a1))
        print("Module 2 Analog.: " + str(a2))
        print("Board Temp......: " + str(round(board_temp_c, 1)) + "C" + \
              " / " + str(round(board_temp_f, 1)) + "F")

        #Wait
        print("-----")
        sleep(0.5)

#Exit on CTRL+C
except KeyboardInterrupt:
    print('Bye.')
