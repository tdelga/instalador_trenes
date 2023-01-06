# Este codigo, escucha el puerto serial, en este caso /dev/pts/2, y en caso de que se envie cualquier dato, apaga el sistema
# instalar la libreria serial con el comando 'pip install pyserial' 

import serial
import os
import time
from serial import SerialException

time_to_check = 10
start_time = time.time()

while True:
    try:
        serBarCode = serial.Serial('/dev/pts/2', 9600, timeout=1)
        # Get the current time
        current_time = time.time()
        time_passed = current_time - start_time

        # Check if the desired amount of time has passed
        if time_passed > time_to_check:
            break
        #read data from serial port
        if(serBarCode.read(4) != b""):
            serBarCode.close()
            os.system("shutdown now")
    except SerialException:
        print("Error al escuchar el puerto serial")
        time.sleep(1)

print("REINICIANDO SERVICIO DESPUES DE 6 HORAS")
# os.system("systemctl restart reader")
