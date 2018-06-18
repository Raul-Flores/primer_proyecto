# CiberC Python Script example

Demo Python Script to config devices

1. Add the execute commands in the directory
commands_file

2. Add the IP addresses of the equipment
that you want to add the commands by modifying
the device_file file.

3. Run the script placing the following
on a computer with python 2.7 installed
python SmarNet-APP-CiberC-1.py

4. The script will execute each of the
commands placed on each listed device
in the devices file, take as an example
some commands and devices added
to see the order in which they should be placed
the same.


Library requirements:
Netmiko
Paramiko
Getpass
datetime


You can install Netmiko it from source:

git clone https://github.com/ktbyers/netmiko.git

cd netmiko

python setup.py install

You can also use pip:

pip install netmiko

pip install paramiko

pip install DateTime
