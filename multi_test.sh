#!/bin/bash

for i in {10..200..10}; 
do
	echo $i
	python test.py --dataroot datasets/zdq_256_bw --name $1 --model cycle_gan --epoch $i > log/test_$1_$i.log
done
