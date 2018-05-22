#!/usr/bin/env python
#Declaramos los modulos a importar
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from datetime import datetime
#Variables para solicitud de usuario y password y enable secret password
username = raw_input('Ingresa tu usuario de SSH: ')
password = getpass('Ingresa tu password de usuario: ')
enablepw = getpass('Coloca el enable Password: ')
#Loop que trae el listado de comandos en un directorio llamado commands_file
with open('commands_file') as f:
    commands_list = f.read().splitlines()
#Loop que trae el listado de equipos que se ingresara en un directorio llamado devices_file
with open('devices_file') as f:
    devices_list = f.read().splitlines()
#Inicia contador de tiempo
start_time = datetime.now()
print '\n\nFecha y hora en que inicia el script:'
print  start_time
#Loop que permite colocar las variables para ingresar a los equipos (a todos)
for devices in devices_list:
    print '\n\n>>>>>>>>> Conectando al dispositivo {0} <<<<<<<<<'.format(devices)
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': username,
        'password': password,
        'secret': enablepw
    }
#Manejador de errores para que el script no se detenga ante un error
    try:
        net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException):
        print 'Fallo de autenticacion en el dispositivo: ' + ip_address_of_device
        continue
    except (NetMikoTimeoutException):
        print 'Timeout (tiempo agotado) en el dispositivo: ' + ip_address_of_device
        continue
    except (EOFError):
        print "Fin del archivo al intentar en el dispositivo " + ip_address_of_device
        continue
    except (SSHException):
        print 'Error de SSH. Estas seguro que esta habilitado en el dispositivo? ' + ip_address_of_device
        continue
    except Exception as unknown_error:
        print 'Algun otro error: ' + str(unknown_error)
        continue
#Ingreso al modo privilegiado
    net_connect.enable()
#Anteponer el simbolo del sistema para el resultado (usado para identificar el host local)
    result = net_connect.find_prompt() + "\n"
#Envio de comandos
    output = net_connect.send_config_set(commands_list)
    print output
    print '#######################'
    print '>>>>>>>>> FIN <<<<<<<<<'
    print '#######################'
#Cerramos el contador de tiempo
    end_time = datetime.now()
    print 'tiempo que tiene el script ejecutado:'
    total_time = end_time - start_time
    print  total_time
#Guardar el ouput generado por dispositivo para ATP
    saveoutput = open("config_" + ip_address_of_device, "w")
    saveoutput.write(output)
    saveoutput.write('\n')
    saveoutput.close
    print 'configuracion guardada para ATP'
#Creado por Raul Flores
#Correo raul.flores@ciberc.com
