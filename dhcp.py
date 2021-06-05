#!/usr/bin/python
# -*- coding:utf8 -*-

### Importation des modules ###
import os
import sys
import fileinput
import configparser
import socket

### Configuration du fichier interfaces ###
with open("/etc/network/interfaces" , "a") as f:
    f.write("\nauto lo\n")
    f.write("iface lo inet loopback\n")
    f.write("\nauto ens3\n")
    f.write("iface ens3 inet static\n")
    f.write("   address 192.168.1.2\n")
    f.write("   netmask 255.255.255.0\n")
    f.write("   gateway 192.168.1.1\n")
    f.write("   dns-nameservers 192.168.1.1\n")
    f.write("\nauto ens4\n")
    f.write("iface ens4 inet static\n")
    f.write("   address 192.168.2.1\n")
    f.write("   netmask 255.255.255.0\n")
    f.write("\nauto ens5\n")
    f.write("iface ens5 inet static\n")
    f.write("   address 192.168.3.1\n")
    f.write("   netmask 255.255.255.0\n")
    f.close()

### Configuration du fichier sysctl.conf ###
file = open("/etc/sysctl.conf" , "r")
lignes = file.readlines()
file.close()
lignes[27] = "net.ipv4.ip_forward=1"
file = open("/etc/sysctl.conf" , "w")
file.writelines(lignes)
file.close()

### Installation des paquets ###
os.system('sudo apt-get update')
os.system('sudo apt-get install isc-dhcp-server')

### Modification du fichier isc-dhcp-server ###
file = open("/etc/default/isc-dhcp-server" , "r")
lignes = file.readlines()
file.close()
lignes[16] = 'INTERFACESv4="ens4 ens5"\n'
file = open("/etc/default/isc-dhcp-server" , "w")
file.writelines(lignes)
file.close()

file = open("/etc/default/isc-dhcp-server" , "r")
lignes = file.readlines()
file.close()
lignes[17] = 'INTERFACESv6="ens4 ens5"'
file = open("/etc/default/isc-dhcp-server" , "w")
file.writelines(lignes)
file.close()

### Configuration du fichier dhcpd.conf ###
