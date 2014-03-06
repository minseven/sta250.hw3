#!/home/nagu/tools/ActivePython/bin/python2.7

import sys
import csv
import nltk

swfile=open(sys.argv[1],'r')
csvfile=open(sys.argv[2],'rb')
reader=csv.reader(csvfile,delimiter=',',quotechar='"')
stopwords=[]
for line in swfile.xreadlines():
	line=line[:-1]
	stopwords.append(line)
for row in reader:
	body=nltk.word_tokenize(row[6])
	title=nltk.word_tokenize(row[7])
	wb=[]
	for i in range(0,len(title)):
		if title[i].lower() not in stopwords and title[i].lower() not in wb:
			wb.append(title[i].lower())
	for i in range(0,len(body)):
		if body[i].lower() not in stopwords and body[i].lower() not in wb:
			wb.append(body[i].lower())
	for w in wb:
		print w
