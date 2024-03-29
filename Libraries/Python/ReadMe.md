# Python Libraries
This directory includes Python libraries for Turta Modular HAT.

## Index
* __Turta_Analog.py:__ Python Library for TI ADS1018 ADC.
* __Turta_Digital.py:__ Python Library for Digital IO Ports.

## Installation of Python Libraries
* Use 'pip3 install turta-modularhat' to download and install libraries automatically.
* Use 'pip3 install --upgrade --user turta-modularhat' to update your libraries.
* Use 'pip3 uninstall turta-modularhat' to uninstall the libraries.
* If you wish to install libraries manually, copy the ingredients of Python folder to the project folder.

## Dependencies for Python Libraries
The package installer installs other libraries required for Modular HAT's operation.
* We're using 'SMBus' for I2C communication. To install it manually, type 'sudo pip3 install smbus' to the terminal.
* We're using 'spidev' for SPI communication. To install it manually, type 'sudo pip3 install spidev' to the terminal.
* We're using 'RPi.GPIO' for GPIO access. To install it manually, type 'pip3 install RPi.GPIO' to the terminal.
* We're using Python 3 for the libraries and samples.

## Raspberry Pi Configuration
* You should enable SPI and I2C from the Raspberry Pi's configuration. To do so, type 'sudo raspi-config' to the terminal, then go to 'Interfacing Options' and enable both SPI and I2C.

## Documentation
Visit [docs.turta.io](https://docs.turta.io) for documentation.
