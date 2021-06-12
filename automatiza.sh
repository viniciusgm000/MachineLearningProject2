#!/bin/bash

for classifier in knn naiveBayes lda lr perceptron; do
    outfile="saidas/"$classifier".out"
    rm $outfile
    for num in 250 500 750 1000 2000 3000 4000 5000 6000 7000 8000 9000 10000 11000 12000 13000 14000 15000 16000 17000 18000 19000 20000; do
        echo $num >> $outfile
        (time python3 $classifier".py" "dados/train"$num".txt" "dados/test.txt") >> $outfile 2>&1
    done
done