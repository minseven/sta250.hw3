#!/usr/bin/python

import sys

wordFile=open(sys.argv[1],'r')
featureFile=open(sys.argv[2],'r')
features=[]
features.append('OwnerUserID')
features.append('ReputationAtPostCreation')
features.append('OwnerUndeletedAnswerCountAtPostTime')
for line in wordFile.xreadlines():
	line=line[:-1]
	features.append(line)	
c=0
for line in featureFile.xreadlines():
	line=line[:-1]
	if c < int(sys.argv[3]):
		print features[int(line)]
	c=c+1
