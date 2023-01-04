SERVICIO LECTOR RFID V2


Requerimientos( no para instalacion, sino funcionamiento)

1- Conexion LAN en PRIMER puerto LAN (enp1s0)

Para correr el instalador ejecute el comando:

sudo python3 insta.py

Esto ejecuta una serie de comandos de forma automatica:

0- Instala git

1- Clona de git el repositorio LECTOR_RFID en /home/user/

2- Instala Java JRE

3- Instala Java JDK

4- Otorga permisos completos al directorio LECTOR_RFID

5- Crear archivo de servicio /etc/systemd/system/reader.service para inicio al booteo de equipo

6- Configura systemctl enable reader , esto habilita el servicio para el booteo

7- Instala librerias para el apagado de equipo por puerto serial

8- Crea servicio para el apagado de equipo por puerto serial

9- Cambia IPv4 de puerto enp1s0 por 192.168.1.201/24

Configuracion final

- En el archivo config.properties ingresar los parametros correspondientes segun la cabina e ip publica del servidor

Si todo salio correctamente el sistema lector queda configurado para iniciar en el inicio del equipo y enviar las lecturas al servidor.
