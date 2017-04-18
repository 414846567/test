#!/usr/bin/python
import paramiko
import os,sys
#from Crypto.Random.OSRNG import winrandom
from scp import SCPClient

#Host = '10.10.36.33'
user = "root"
passwd = "p@ssw0rd0cean"
port =9999
for HOST in sys.argv[1:]:
	scpclient = SCPClient(ssh.get_transport(), socket_timeout=15.0)
	remotepath='/root/Writepic'
	localpath='/root/'
	scpclient.put(localpath, remotepath)
#localpath1 = 'get.txt'
#scpclient.get(remotepath, localpath1)
	ssh.close()
#for index,tt in enumerate(st):
#    print(index,tt)
