#!/home/minseven/bin/python

import sys
import sklearn.metrics

file=open(sys.argv[1],'r')
out=open(sys.argv[2],'w')
mi=[]
first=True
classArray=[]
index=0
for line in file.xreadlines():
	line=line[:-1]
	element=line.split('\t')
	if first == True:
		classArray=element
		first=False
		continue
	mi.append((index,sklearn.metrics.mutual_info_score(classArray,element)))
	index=index+1
mi=sorted(mi,reverse=True,key=lambda x: x[1])
for i in range(0,len(mi)):
	out.write(str(mi[i][0])+'\n')
