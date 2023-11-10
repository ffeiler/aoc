# SOLUTION FOR DAY 1 OF 2017
# Riddle @ https://adventofcode.com/2017/day/1
# ============================

import numpy as np

input_path = "data/raw/2017/1.txt"
with open(input_path, "r") as f:
    data = f.read().strip()


# TASK 1
d1 = [int(x) for x in data]
d1.append(d1[0])

sum_eq_1 = 0
for j, k in zip(d1[:-1], d1[1:]):
    if j == k:
        sum_eq_1 += j
print(sum_eq_1)

# TASK 2
d2 = [int(x) for x in data]
offset = len(data) // 2

for i in range(offset):
    d2.append(d2[i])

sum_eq_2 = 0
for j, k in zip(d2[:-offset], d2[offset:]):
    if j == k:
        sum_eq_2 += j
print(sum_eq_2)
