#!/bin/bash
cd  /home/user/LECTOR_RFID/
echo "Checkeando si hay un update"
git remote update 

sleep 5

UPSTREAM=${1:-'@{u}'}
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse "$UPSTREAM")
BASE=$(git merge-base @ "$UPSTREAM")

if [ $LOCAL = $REMOTE ]; then
    echo "Up-to-date"
elif [ $LOCAL = $BASE ]; then
    echo "Need to pull"
    git pull https://github.com/tdelga/instalador_trenes.git
else
    echo "Diverged"
fi

sleep 10
echo Servicio levantado
python3 rs232_recibe.py &
java -jar /home/user/LECTOR_RFID/Lector_v1.jar
echo Servicio levantado

