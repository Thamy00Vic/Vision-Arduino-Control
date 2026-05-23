import serial
import time

arduino = serial.Serial('COM3', 9600)
time.sleep(2)

while True:

    comando = input("Digite 1 para ligar ou 0 para desligar: ")

    if comando == "1":
        arduino.write(b'1')

    if comando == "0":
        arduino.write(b'0')