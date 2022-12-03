#!/bin/bash
cd  /home/user/LECTOR_RFID/
git pull https://github.com/tdelga/instalador_trenes.git
sleep 30
python rs232_recibe.py
java -jar /home/user/LECTOR_RFID/Lector_v1.jar
