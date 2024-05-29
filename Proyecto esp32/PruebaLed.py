import serial
import time 

ser = serial.Serial("/dev/ttyUSB0", 9600)  # Puerto serial en la Raspberry Pi

while True:
    command = input("Ingrese '1' para encender el LED o '0' para apagarlo: ")
    if command == '1' or command == '0':
        ser.write(command.encode())
        time.sleep(0.5)
    else:
        print("Entrada no válida. Ingrese '1' o '0'.")
