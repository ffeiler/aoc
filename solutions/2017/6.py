# SOLUTION FOR DAY 6 OF 2017
# Riddle @ https://adventofcode.com/2017/day/6
# ============================

import numpy as np

input_path = "data/raw/2017/6.txt"
with open(input_path, "r") as f:
    data = f.read().strip().split("\t")
data = [int(x) for x in data]


# ========= TEST 1 =========
def test1(cfg):
    wrap = len(cfg)
    cfgs = []
    counter = 0
    while cfg not in cfgs:
        c = cfg.copy()
        cfgs.append(cfg)
        max_pos = np.argmax(c)
        v = c[max_pos]
        c[max_pos] = 0
        for i in range(1, v + 1):
            c[(max_pos + i) % wrap] += 1
        counter += 1
        cfg = c
    return counter


# ========= TEST 2 =========
def test2(cfg):
    wrap = len(cfg)
    cfgs = []
    counter = 0
    while cfg not in cfgs:
        c = cfg.copy()
        cfgs.append(cfg)
        max_pos = np.argmax(c)
        v = c[max_pos]
        c[max_pos] = 0
        for i in range(1, v + 1):
            c[(max_pos + i) % wrap] += 1
        counter += 1
        cfg = c
    sim_matrix = np.array(cfgs) == cfg
    first_occurence = np.where(sim_matrix.sum(axis=1) == wrap)[0][0]
    diff = counter - first_occurence
    return diff


test_data = [0, 2, 7, 0]
assert test1(test_data) == 5
print(f"Test 1: {test1(data)} steps before a config has seen before")

assert (test2(test_data)) == 4
print(f"Test 2: {test2(data)} steps between the same configs")
