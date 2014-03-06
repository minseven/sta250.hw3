#!/usr/bin/python

import sys

file=open(sys.argv[1],'r')
out=open(sys.argv[2],'w')
nline=''
pos=int(sys.argv[3])
for line in file.xreadlines():
	line=line[:-1]
	element=line.split('\t')
	nline=nline+element[pos]+'\t'
out.write(nline[:-1]+'\n')
