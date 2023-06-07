#!/usr/bin/python
#####Pull Request testing#######
#encoding=utf-8
import ConfigParser
 
 
#reading configration files
config = ConfigParser.ConfigParser()
config.readfp(open("config","rb"))
 
g_ip = config.get("computer","ip")
g_port = config.get("computer","port")
 
print ("IP:",g_ip,"PORT:",g_port)
