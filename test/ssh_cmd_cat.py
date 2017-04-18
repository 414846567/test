#-*- coding: utf-8 -*-
#!/usr/local/bin/python
import paramiko
import threading
import pexpect
import sys,os
from fabric.api import env,put,get


username = "root"
passwd = "p@ssw0rd0cean"
#ip2="10.10.36.41"
def ssh2(ip,username,passwd,cmd):
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(ip,9999,username,passwd,timeout=10)
		for m in cmd:
		  stdin,stdout,stedrr = ssh.exec_command(m)
		  stdin.write("Y")
		  out = stdout.readlines()
		  for o in out:
	          	print o,
		print '%s\tOK\n'%(ip)
		ssh.close()
	except:
		print '%s\tError\n'%(ip)

def upload(uSRC,uDST):
		env.user=username
		env.password=passwd
		env.host_string=ip
		env.port=9999
		#with hide('running'):
		put("%s" %(uSRC),"%s" %(uDST))
		#for ip in IP_PORT:
		#env.host_string=self.ip
		#print "Upload local file : \"%s\" to Host : %s \"%s\"" %(uSRC,self.ip.split(':')[0],uDST)
		print "successful!!!\n"

def download(dSRC,dDST):
		env.user=username
		env.password=passwd
		env.host_string=ip2
		get("%s" %(dSRC),"%s" %(dDST))
		print "successful!!!\n"
 

if __name__=='__main__':
#     threads=[]
#     app="digioceanfs-3.8.1-34"
#     cmd=["node-manager clear","for i in `rpm -qa|grep digiocean`;do yum -y remove $i;done ","cd /root/%s&&yum -y install *.rpm"%app,"node-manager start"]
#    ip=sys.argv[1]
     cmd = ["ipmitool lan print"]
     for ip in sys.argv[1:]:
#        for ip in list:
	#if len(sys.argv) < 3:
	#	print "please enter:upload,ssh,download"
#	for ip in list:
#	if sys.argv[1]=='upload':
#	s = a = ip.split(".")[3]
#	str(s),str(a)
#	a = ip.split(3)[3]
#	s = threading.Thread(target=upload,args=("/root/digi/%s"%app,"/root"))
#	s.start()
	print "%s:"%ip
        ssh2(ip,username,passwd,cmd)
#	a.start()
"""
#	elif sys.argv[1] == 'ssh':
#	for ip in list:
	      cmd = argv[2]
	      a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
	      a.start()
	elif sys.argv[1] == 'download':
#		for ip in list:
	      t = threading.Thread(target=download,args=(uSRC,uDST))	
	      t.start()
  	else:
	      print "error"
"""
