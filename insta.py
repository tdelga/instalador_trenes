
import os

directory = '/home/user/'

try:

  # 0
  print('Iniciando proceso de instalacion')
  os_cmd = ' apt install git -y'
  if os.system(os_cmd) != 0:
    raise Exception()
  print("Instalacion iniciada")
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    
  # 1
  if(not os.path.isdir(directory + 'LECTOR_RFID')):
    print('1/9 - Clonando respositorio LECTOR_RFID para iniciar instalacion')
    os_cmd = ' git clone https://github.com/Tyrrell01/Repositorio_01_RFID.git ' + directory + 'LECTOR_RFID'
    os_cmd2 = ' git config --global --add safe.directory ' + directory + 'LECTOR_RFID'
    if os.system(os_cmd) != 0:
        raise Exception()
    if os.system(os_cmd2) != 0:
        raise Exception()
    print("1/9- Proyecto clonado exitosamente")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


  # 2
  print('2/9 - Instalando Java JRE')
  os_cmd = 'apt install default-jre -y'
  if os.system(os_cmd) != 0:
      raise Exception()
  print("2/9 - Instalado Java JRE exitosamente")
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

  # 3
  print('3/9 - Instalando Java JDK')
  os_cmd = 'apt install default-jdk -y'
  if os.system(os_cmd) != 0:
      raise Exception()
  print("3/9 - Instalado Java JDK exitosamente")
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

  # 4
  print('4/9 - Otorgando permisos completos al directorio')
  os_cmd = 'chmod 777 -R ' + directory + 'LECTOR_RFID ./.[!.]*'
  if os.system(os_cmd) != 0:
      raise Exception()
  print(" 4/9 - Otorgados permisos completos al directorio exitosamente")
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

  # 5
  if(not os.path.isfile(directory + 'LECTOR_RFID')):
    print('5/9 - Creando servicio de lector RFID')
    os_cmd = 'cp ' + directory + 'LECTOR_RFID/'+ 'reader.service /etc/systemd/system/'
    if os.system(os_cmd) != 0:
        raise Exception()
    print(" 5/9 - Servicio de lector creado exitosamente")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

  # 6
  print('6/9 - Configurando Servicio de lector para booteo')
  os_cmd = 'systemctl enable reader'
  if os.system(os_cmd) != 0:
      raise Exception()
  print(" 6/9 - Servicio de lector configurado para booteo exitosamente")
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

  # 7
  print('7/9 - Instalando librerias de apagado por puerto serial')
  os_cmd = 'apt install python3-pip -y'
  if os.system(os_cmd) != 0:
      raise Exception()
  print(" 7/9 - Librerias instaladas exitosamente")
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

  # 8
  print('8/9 - Configurando servicio de apagado por puerto serial')
  os_cmd = 'pip3 install pyserial'
  if os.system(os_cmd) != 0:
      raise Exception()
  print(" 9/9 - Servicio de apagado por puerto serial instalado configurado exitosamente")
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


except:
  print("Instalacion abortada")


