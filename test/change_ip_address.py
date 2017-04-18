#-*- coding: utf-8 -*-
#!/usr/local/bin/python
import paramiko
import threading
import pexpect
import sys,os
import subprocess
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

     for ip in sys.argv[1:]:
	s = ip.split(".")[3]
	cmd=['sed -i "s/dhcp/static/;s/PEERDNS=yes/PEERDNS=no/;s/IPV6_PEERDNS=yes/IPV6_PEERDNS=no/;s/ONBOOT=no/ONBOOT=yes/g" /etc/sysconfig/network-scripts/ifcfg-enp6s0f0','echo -e "IPADDR=192.168.1.%s\nNM_CONTROLLED=no\n" >>/etc/sysconfig/network-scripts/ifcfg-enp6s0f0'%s,'systemctl restart network']
	print cmd
        ssh2(ip,username,passwd,cmd)
