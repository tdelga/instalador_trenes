#!/bin/bash

python rs232_recibe.py
sleep 30
java -jar /home/user/LECTOR_RFID/Lector_v1.jar
