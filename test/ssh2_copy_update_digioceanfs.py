#-*- coding: utf-8 -*-
#!/usr/local/bin/python
import paramiko
import threading
import pexpect
import sys,os
import subprocess
from fabric.api import env,put,get
import time


username = "root"
passwd = "asdf"
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

def upload(uSRC,uDST,ip):
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
# try:
     threads=[]
     #print "上传文件到各个节点："
     #cmd1="ls -t /rpm|awk NR==1{print}"
     #tmp=subprocess.Popen(cmd1,shell=True,stdout=subprocess.PIPE)
#     temp.wait()
     app="DOFS-3.8.1-031052.tar.gz"
     #cmd=["node-manager clear","for i in `rpm -qa|grep digiocean`;do yum -y remove $i;done ","tar -zxvf /root/%s|xargs -I {} yum -y install {}"%app,"node-manager start"]
     #cmd=["tar -zxvf /root/%s|xargs -I {} yum -y install {}"%app]
    # cmd=["node-manager stop","for i in `rpm -qa|grep digiocean`;do yum -y remove $i;done;rpm -qa|grep digiocean "]
     #cmd=["yum -y install /root/digi/DOFS-3.8.1-031052/*.rpm"]
     for ip in sys.argv[1:]:
	s = threading.Thread(target=upload,args=("/root/digi/","/root",ip))
	threads.append(s)
     for i in range(len(sys.argv[1:])):
	threads[i].start()
     for i in range(len(sys.argv[1:])):
	threads[i].join()
       # a = threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
	#a.start()
# except Exception,e:

#     print "ok"
