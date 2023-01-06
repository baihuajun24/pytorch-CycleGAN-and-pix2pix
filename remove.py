import os
import re

path = "/root/autodl-tmp/pytorch-CycleGAN-and-pix2pix/checkpoints/zdq_256_blackwhite/"
f = sorted(os.listdir(path))
# print(f)
digit = []
for i in f:
    if len(re.findall(r"\d+\.?\d*", i)) != 0:
        digit.append(i)
# print(digit)
res = []
for i in digit:
    if int(re.findall(r"\d+\.?\d*", i)[0]) < 175:
        res.append(i)
# print(res)
for i in res:
    os.system(f"rm {path}{i}")
    