import serial
import time

ser = serial.Serial('COM3', 9600)  # Replace with the appropriate serial port

while True:
    angle = int(input('Enter the angle (0-180): '))
    ser.write(str(angle).encode())
    time.sleep(1)
