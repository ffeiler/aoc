# SOLUTION FOR DAY 1 OF 2024
# Riddle @ https://adventofcode.com/2024/day/1
# ============================

import numpy as np

input_path = "data/raw/2024/1.txt"
with open(input_path, "r") as f:
    data = f.read().strip().split("\n")


# ========= HELPERS =========


def split_into_lists(data):
    all_data = [x.split("   ") for x in data]
    all_data = np.array(all_data).flatten()
    left_list = all_data[::2]
    right_list = all_data[1::2]
    return left_list, right_list


def list_str_to_int(x):
    return [int(s) for s in x]


def abs_dist(x, y):
    return abs(x - y)


# ========= TESTING DATA =========
example_data = ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]


# ========= TEST 1 =========
def test1(data):
    left, right = split_into_lists(data)

    left = np.sort(list_str_to_int(left))
    right = np.sort(list_str_to_int(right))

    dist = [abs_dist(x, y) for x, y in zip(left, right)]
    return sum(dist)


assert test1(example_data) == 11
print(f"Solution for d1/t1: {test1(data)}")


# ========= TEST 2 =========
def test2(data):
    left, right = split_into_lists(data)

    left = list_str_to_int(left)
    right = list_str_to_int(right)

    unique, counts = np.unique(right, return_counts=True)
    right_occ_dict = dict(zip(unique, counts))
    sim = [x * right_occ_dict.get(x, 0) for x in left]
    return sum(sim)


assert test2(example_data) == 31
print(f"Solution for d1/t2: {test2(data)}")
