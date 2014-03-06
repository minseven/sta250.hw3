#!/home/minseven/bin/python

import sys
import sklearn.metrics
import collections

def predictClassLabel(array):
	darray=[]
	for i in range(0,len(trainData)):
		d=sklearn.metrics.pairwise.pairwise_distances([array[1:]],[trainData[i][1:]],metric='correlation')
		darray.append((trainData[i][0],d[0][0]))
	darray=sorted(darray,reverse=False,key=lambda x: x[1])
	classes=[]
	for i in range(0,K):
		classes.append(darray[i][0])
	classes=collections.Counter(classes)
	value,count=classes.most_common()[0]
	return value

sortedFeatureFile=open(sys.argv[1],'r')
trainFile=open(sys.argv[2],'r')
testFile=open(sys.argv[3],'r')
THRESHOLD=int(sys.argv[4])
K=int(sys.argv[5])
out=open(sys.argv[6],'w')
count=1
featureIndices={}
for line in sortedFeatureFile.xreadlines():
	line=line[:-1]
	if count == THRESHOLD:
		break
	else:
		featureIndices[int(line)]=1
		count=count+1
trainData=[]
count=1
for line in trainFile.xreadlines():
	line=line[:-1]
	element=line.split('\t')
	array=[]
	array.append(element[0])
	for i in range(1,len(element)):
		try:
			v=featureIndices[i]
			array.append(int(element[i]))
		except:
			continue
	print 'storing trainData '+str(count)
	count=count+1
	trainData.append(array)
TP=0
FP=0
FN=0
TN=0
count=1
for line in testFile.xreadlines():
	line=line[:-1]
	element=line.split('\t')
	array=[]
	array.append(element[0])
	for i in range(1,len(element)):
		try:
			v=featureIndices[i]
			array.append(int(element[i]))
		except:
			continue
	predicted=predictClassLabel(array)
	if predicted == array[0] and array[0] == 'closed':
		TP=TP+1
	elif predicted != array[0] and array[0] == 'open':
		FP=FP+1
	elif predicted != array[0] and array[0] == 'closed':
		FN=FN+1
	else:
		TN=TN+1
	if predicted == array[0]:
		print 'count '+str(count)+' correct'
	else:
		print 'count '+str(count)+' incorrect'
	count=count+1
out.write('THR: '+str(THRESHOLD)+' K: '+str(K)+' TP: '+str(TP)+' FP: '+str(FP)+' FN: '+str(FN)+' TN: '+str(TN)+' Accuracy: '+str(float(TP+TN)/float(TP+FP+FN+TN))+'\n')
