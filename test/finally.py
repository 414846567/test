#!/usr/bin/python
import time
try:
	f=open("poem.txt","r")
	while True:
		line=f.readline()
		if len(line)==0:
			break
		time.sleep(2)
		print line
finally:
	f.close()
	print "Cleanling up.......closed the file"
