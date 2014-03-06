#!/home/nagu/tools/ActivePython/bin/python2.7

import sys
import csv
import nltk

word_file=open(sys.argv[1],'r')
csv_file=open(sys.argv[2],'rb')
index_file=open(sys.argv[3]+'.index.txt','w')
out_file=open(sys.argv[3]+'.matrix.txt','w')
reader=csv.reader(csv_file,delimiter=',',quotechar='"')
words={}
THRESHOLD=30
for line in word_file.xreadlines():
	line=line[:-1]
	element=line.split('\t')
	if int(element[0]) > THRESHOLD:
		index_file.write(element[1]+'\n')
		words[element[1]]=1
first=True
for row in reader:
	if first == True:
		first=False
		continue
	body=nltk.word_tokenize(row[6])
	title=nltk.word_tokenize(row[7])
	nline=row[14]+'\t'+row[2]+'\t'+row[4]+'\t'+row[5]
	wb={}
	for i in range(0,len(title)):
                if title[i].lower() not in wb:
                        wb[title[i].lower()]=1
        for i in range(0,len(body)):
                if body[i].lower() not in wb:
                        wb[body[i].lower()]=1
	for word in words:
		try:
			t=wb[word]
			nline=nline+'\t1'
		except:
			nline=nline+'\t0'
	out_file.write(nline+'\n')
