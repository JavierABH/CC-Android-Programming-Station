import serial
import time

arduino = serial.Serial('COM8', 9600)
time.sleep(2)

# PIN ON
arduino.write(b'H')
print("ON...")
time.sleep(5)

# PIN OFF
arduino.write(b'L')
print("OFF...")

arduino.close()
