#!/usr/bin/python

import sys

file=open(sys.argv[1],'r')
for line in file.xreadlines():
	line=line[:-1]
	element=line.split('\t')
	print line+'\t'+str(float(element[4])/float(element[3]))
