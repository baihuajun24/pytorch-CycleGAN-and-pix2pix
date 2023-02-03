for i in $(seq 0.0 0.1 1.0)
#$(seq 1.0 .01 1.1)
do
#echo $i
e_name="freeze-rate_${i}"
rate=$i
#echo $rate is $(float_eval "$rate")
bash make_ckpt.sh $e_name > log/make_ckpt_$e_name.log
python train.py --dataroot datasets/zdq_256_bw --name $e_name --model cycle_gan --continue_train --freeze_rate $rate > log/$e_name.log
bash multi_test.sh $e_name
python visualization.py $e_name
done
