#!/bin/bash
for i in $(seq 0.5 0.1 1.0)
do
	e_name="freeze-rate_${i}"
	echo $e_name
	for i in {10..200..10}; 
	do
		echo $i
		python test.py --dataroot datasets/zdq_256_bw --name $e_name --model cycle_gan --epoch $i > log/test_$e_name_$i.log
	done
done
