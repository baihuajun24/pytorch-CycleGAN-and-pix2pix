# copy pretrain model ckpt for new fine-tune experiments
mkdir checkpoints/$1
cp checkpoints/freeze-finetune/200_net_D_A.pth checkpoints/$1
cp checkpoints/freeze-finetune/200_net_D_B.pth checkpoints/$1
cp checkpoints/freeze-finetune/200_net_G_A.pth checkpoints/$1
cp checkpoints/freeze-finetune/200_net_G_B.pth checkpoints/$1
