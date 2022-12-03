SERVICIO LECTOR RFID

Requerimientos

1- Conexion LAN en PRIMER puerto

2- IPv4 manual LAN 192.168.1.201

Para correr el instalador ejecute el comando:

sudo python3 insta.py

Esto ejecuta una serie de comandos de forma automatica:

1- Crea el proyecto LECTOR_RFID en /home/user/

2- Instala Java JRE

3- Instala Java JDK

4- Otorga permisos completos al directorio

5- Crear archivo de servicio /etc/systemd/system/reader.service para inicio al booteo de equipo

6- systemctl enable reader , esto habilita el servicio para el booteo

7- Instala librerias para el apagado de equipo por puerto serial

8- Crea servicio para el apagado de equipo por puerto serial

9- Cambia IP de puerto LAN

Configuracion final

- En el archivo config.properties ingresar los parametros correspondientes segun la cabina e ip publica del servidor

Si todo salio correctamente el sistema lector queda configurado para iniciar en el inicio del equipo y enviar las lecturas al servidor.
