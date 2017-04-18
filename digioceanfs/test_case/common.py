#! -*- coding:utf-8 -*-
from datetime import datetime
from selenium import webdriver

def browers():
	return webdriver.Firefox()
		
def baseurl():
	return "https://10.10.16.22/"

def lic_url():
	return "http://10.10.1.15/license"

def username():
	return "admin" 
def passwd():
	return "12345678"
def node_num():
	nodes=len(file("../test_data/node_list_file","r").readlines())
	return nodes
	
"""
def getcurrenttime():
	format="%a %b %d %H:%M:%S %y"
	return datetime.now().strftime(format)

def timediff(starttime,endtime):
	format="%a %b %d %H:%M:%S %y"
	return datetime.strptime(endtime,format) - datetime.strptime(starttime,format) 
"""
