#!/bin/bash

for i in {10..200..10}; 
do
	echo $i
python test.py --dataroot /root/autodl-tmp/pytorch-CycleGAN-and-pix2pix/datasets/zdq_256_bw --name freeze-finetune --model cycle_gan --epoch $i > log/test_$i.log
done
