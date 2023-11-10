# SOLUTION FOR DAY 2 OF 2017
# Riddle @ https://adventofcode.com/2017/day/2
# ============================

import numpy as np

input_path = "data/raw/2017/2.txt"

with open(input_path, "r") as f:
    data = f.read().strip()

# Part 1
# -------

# test1 = "5\t1\t9\t5\n7\t5\t3\n2\t4\t6\t8\n".strip()
lines = [l for l in data.split("\n")]
lines = [[int(x) for x in l.split("\t")] for l in lines]
l_sort = [sorted(l, reverse=True) for l in lines]
l_diff = [l[0] - l[-1] for l in l_sort]
checksum = sum(l_diff)
print(f"Checksum for task 1: {checksum}")


# Part 2
# -------


def check_divisible(items: list):
    divs = []
    for i, item in enumerate(items):
        others = items[i + 1 :]
        for o in others:
            if item % o == 0:
                divs.append(item // o)
    return divs


# test2 = "5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5\n".strip()
lines = [l for l in data.split("\n")]
lines = [[int(x) for x in l.split("\t")] for l in lines]
l_sort = [sorted(l, reverse=True) for l in lines]
l_divs = [sum(check_divisible(l)) for l in l_sort]
checksum = sum(l_divs)
print(f"Checksum for task 2: {checksum}")
