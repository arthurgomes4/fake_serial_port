import serial
import time

# send a message once every second to /dev/device and print the response to console
ser = serial.Serial('/dev/device', 19200)

while True:
    ser.write(b'Hello, world!\n')
    print('Sent message: Hello, world!')
    print('got message: ',ser.readline())
    time.sleep(1)