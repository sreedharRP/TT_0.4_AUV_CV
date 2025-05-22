import serial
import time

ser = serial.Serial('COM9', 9600)

Thurster_1 = "M1"
Thruster_Speed = 1000

Thuster_comand = Thurster_1 +","+ str(Thruster_Speed)+ "\n"

a = []

ser.close()
ser.open()

while True:   
    # with open("data.txt", "r") as file:
    #         a = file.readlines()
            if len(Thuster_comand) == 8:
                data = ser.write(Thuster_comand.encode())
                print("Sent")
            print(data)
