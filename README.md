1. measure frequencies of words that appear in the dataset (removing stopwords)

./getWords.py stopwords.txt train-sample.csv | sort | uniq -c | sort -k 1 -g -r | awk '{print $1 "\t" $2}' > wordfreq-sample.txt

2. construct the matrix where column represent binary occurrence of word that appears more than 20 data (that is, 20 StackOverflow questions) and features of ReputationAtPostCreation, OwnerUndeletedAnswerCountAtPostTime are also included with open status.

./getMatrix.py wordfreq-sample.txt train-sample.csv train-sample

3. split the matrix into three folds and change the class label of non ‘open’ status into ‘closed’.

./getSplit.sh train-sample.matrix

4. transpose the matrix to readily compute the mutual information between feature and class label.

NCOL=head –n 1 train-sample.matrix.1.txt | awk ‘{print NF}’
for i in $(seq 0 1 $(($NCOL-1)))
do
	./getTranspose.py train-sample.matrix.1.txt $i train-sample.matrix.1.t${i}.txt
done  

for i in $(seq 0 1 $(($NCOL-1)))
do
	cat train-sample.matrix.1.t${i}.txt >> train-sample.matrix.1.t.txt
done  

5. get mutual information of each feature in descending order from train data

./getFeatues.py train-sample.matrix.1.t.txt train-sample.sortedFeatures.1.txt

6. train KNN by varying K and number of (most informative) features selected. Distance metric used here is pearson correlation.

for k in 1 5 10
do
for m in 10 50 100 150
do 
./getKNN.py train-sample.sortedFeatures.txt train-sample.matrix.1.txt train-sample.matrix.2.txt $m $k train-sample.matrix.l1t2.m${m}.k${k}.log
done 
done

7. test using optimized parameters of K and number of (most informative) features selected

for k in 1 5 10
do
for m in 10 50 100 150
do 
./getKNN.py train-sample.sortedFeatures.txt train-sample.matrix.1.txt train-sample.matrix.3.txt $m $k train-sample.matrix.l1t3.m${m}.k${k}.log
done 
done

