
import os

directory = '/home/fran/'

try:
    
  # 1
  if(not os.path.isdir(directory + 'LECTOR_RFID')):
    print('1/8 - Clonando respositorio LECTOR_RFID para iniciar instalacion')
    os_cmd = ' git clone https://github.com/tdelga/instalador_trenes.git ' + directory + 'LECTOR_RFID'
    if os.system(os_cmd) != 0:
        raise Exception()
    print("1/8- Proyecto clonado exitosamente")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

  # 2
  print('2/8 - Instalando Java JRE')
  os_cmd = 'apt install default-jre -y'
  if os.system(os_cmd) != 0:
      raise Exception()
  print("2/8 - Instalado Java JRE exitosamente")
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

  # 3
  print('3/8 - Instalando Java JDK')
  os_cmd = 'apt install default-jdk -y'
  if os.system(os_cmd) != 0:
      raise Exception()
  print("3/8 - Instalado Java JDK exitosamente")
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

  # 4
  print('4/8 - Otorgando permisos completos al directorio')
  os_cmd = 'chmod 777 ' + directory + 'LECTOR_RFID'
  if os.system(os_cmd) != 0:
      raise Exception()
  print(" 4/8 - Otorgados permisos completos al directorio exitosamente")
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

  # 5
  if(not os.path.isfile(directory + 'LECTOR_RFID')):
    print('5/8 - Creando servicio de lector RFID')
    os_cmd = 'cp ' + directory + 'LECTOR_RFID/'+ 'reader.service /etc/systemd/system/'
    if os.system(os_cmd) != 0:
        raise Exception()
    print(" 5/8 - Servicio de lector creado exitosamente")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

  # 6
  print('6/8 - Configurando Servicio de lector para booteo')
  os_cmd = 'systemctl enable reader'
  if os.system(os_cmd) != 0:
      raise Exception()
  print(" 6/8 - Servicio de lector configurado para booteo exitosamente")
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

  # 7
  print('7/8 - Instalando librerias de apagado por puerto serial')
  os_cmd = 'apt install python3-pip -y'
  if os.system(os_cmd) != 0:
      raise Exception()
  print(" 7/8 - Librerias instaladas exitosamente")
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

  # 8
  print('8/8 - Configurando servicio de apagado por puerto serial')
  os_cmd = 'pip3 install pyserial'
  if os.system(os_cmd) != 0:
      raise Exception()
  print(" 8/8 - Servicio de apagado por puerto serial instalado configurado exitosamente")
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

  print("Instalacion finalizada correctamente!")

except:
  print("Instalacion abortada")


