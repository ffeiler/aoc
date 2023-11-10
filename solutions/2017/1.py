# SOLUTION FOR DAY 1 OF 2017
# Riddle @ https://adventofcode.com/2017/day/1
# ============================

import numpy as np

input_path = "data/raw/2017/1.txt"
with open(input_path, "r") as f:
    data = f.read().strip()

data = [int(x) for x in data]
data.append(data[0])

sum_eq = 0
for j, k in zip(data[:-1], data[1:]):
    if j == k:
        sum_eq += j

print(sum_eq)
