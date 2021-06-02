#!/usr/bin/python
# -*-coding:utf8 -*

import os
import os.path
import sys
import fileinput
import configparser
import socket

### Installation des paquets ###
os.system('sudo apt-get update')
os.system('sudo apt-get install isc-dhcp-server')
