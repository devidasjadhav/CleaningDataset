#!/usr/bin/python
import sys
from os import listdir
print sys.argv[1]

def num(x):
	return float(x) if '.' in x else int(x)


for filename in listdir("./"+ sys.argv[1]):
	f = open("./"+ sys.argv[1] + "/" + filename , 'r')
	d = {}
	dc = {}
	f.readline()
	rid = ((f.readline()).rstrip()).split(",")[2]
	for l in f:
		l = (l.rstrip()).split(",")
		if d.has_key(l[1]):
			d[l[1]] =  d[l[1]] + num(l[2])
			dc[l[1]] =  dc[l[1]] + 1
		else:
			d[l[1]]  =  num(l[2])
			dc[l[1]] =  1

	d = dict((k, float(d[k]) / dc[k]) for k in dc)
	print  "\n:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n" + rid + "\n:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"  
	print d 
	f.close()



