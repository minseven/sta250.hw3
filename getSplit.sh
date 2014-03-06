#!/bin/bash

filename=$1

grep open ${filename}.txt > ${filename}.open.txt
grep -v open ${filename}.txt | sed -e 's/not a real question/closed/' -e 's/not constructive/closed/' -e 's/off topic/closed/' -e 's/too localized/closed/' > ${filename}.closed.txt

echo separate open and closed into two files

for type in open closed
do
	head -n 23378 ${filename}.${type}.txt > ${filename}.${type}.1.txt
	head -n 46756 ${filename}.${type}.txt | tail -n 23378 > ${filename}.${type}.2.txt
	tail -n 23380 ${filename}.${type}.txt > ${filename}.${type}.3.txt
done

echo split into 3 files for each of open and closed files

for i in 1 2 3
do 
	cat ${filename}.open.$i.txt ${filename}.closed.$i.txt > ${filename}.$i.txt
done

echo merge into one file for a fold
