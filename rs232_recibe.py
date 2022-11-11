# Este codigo, escucha el puerto serial, en este caso /dev/pts/2, y en caso de que se envie cualquier dato, apaga el sistema
# instalar la libreria serial con el comando 'pip install pyserial' 

import serial
import os
serBarCode = serial.Serial('/dev/pts/2', 9600, timeout=1)

while True:

    #read data from serial port
        
        if(serBarCode.read(4) != b""):
                serBarCode.close()
                os.system("shutdown now")

