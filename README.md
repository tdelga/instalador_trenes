Configuracion y Ejecucion

1- Descarga el proyecto en /home/user/instalador_trenes

2- Otorga permisos completos al directorio

2- Crear archivo de servicio en la ruta /etc/systemd/system/ llamado reciber.service con siguiente contenido (template en el repo)

4- systemctl enable reciber , esto habilita el servicio para el booteo

PARA TESTEO systemctl start reciber