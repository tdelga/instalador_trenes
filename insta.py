
import os

try:
  # 1
  print('1/7 - Creando el proyecto')
  os_cmd = 'mkdir /home/user/LECTOR_RFID'
  if os.system(os_cmd) != 0:
      raise Exception()
  print("1/7- Creado el proyecto LECTOR_RFID en /home/user/")

  # 2
  print('2/7 - Instalando Java JRE')
  os_cmd = 'sudo apt install default-jre'
  if os.system(os_cmd) != 0:
      raise Exception()
  print("2/7 - Instalado Java JRE exitosamente")

  # 3
  print('3/7 - Instalando Java JDK')
  os_cmd = 'sudo apt install default-jdk'
  if os.system(os_cmd) != 0:
      raise Exception()
  print("3/7 - Instalado Java JDK exitosamente")

  # 4
  print('4/7 - Otorgando permisos completos al directorio')
  os_cmd = 'sudo chmod 777 /home/user/LECTOR_RFID'
  if os.system(os_cmd) != 0:
      raise Exception()
  print(" 4/7 - Otorgados permisos completos al directorio exitosamente")

  # 5
  print('5/7 - Creando servicio de lector RFID')
  os_cmd = 'cp -r ...'
  if os.system(os_cmd) != 0:
      raise Exception()
  print(" 5/7 - Servicio de lector creado exitosamente")

  # 6
  print('6/7 - Configurando Servicio de lector para booteo')
  os_cmd = 'sudo systemctl enable reader'
  if os.system(os_cmd) != 0:
      raise Exception()
  print(" 6/7 - Servicio de lector configurado para booteo exitosamente")

  # 7
  print('7/7 - Configurando servicio de apagado por puerto serial')
  os_cmd = 'sudo chmod 777 /home/user/LECTOR_RFID'
  if os.system(os_cmd) != 0:
      raise Exception()
  print(" 7/7 - Servicio de apagado por puerto serial instalado configurado exitosamente")

except:
  print("Instalacion abortada")


