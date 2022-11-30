SERVICIO LECTOR RFID

Requerimientos

1- Conexion LAN en PRIMER puerto

2- IPv4 manual LAN 192.168.1.201

Configuracion y Ejecucion

- En el archivo config.properties ingresar los parametros correspondientes segun la cabina e ip publica del servidor

- Ejecutar comando sudo ./instalador.sh

Esto ejecuta una serie de comandos de forma automatica:

1- Crea el proyecto LECTOR_RFID en /home/user/

2- Instala Java JRE

3- Instala Java JDK

4- Otorga permisos completos al directorio

5- Crear archivo de servicio /etc/systemd/system/reader.service para inicio al booteo de equipo

6- systemctl enable reader , esto habilita el servicio para el booteo

7- Crea servicio para el apagado de equipo por puerto serial

Si todo salio correctamente el sistema lector queda configurado para iniciar en el inicio del equipo y enviar las lecturas al servidor.
