import serial 
import pyfirmata
import sys
import time


# Set up the board
board = pyfirmata.Arduino('COM4')

# Set up the pin
pin13 = board.get_pin('d:13:o')

# Turn on the pin
pin13.write(1)
