# SOLUTION FOR DAY 4 OF 2017
# Riddle @ https://adventofcode.com/2017/day/4
# ============================

import numpy as np

input_path = "data/raw/2017/4.txt"
with open(input_path, "r") as f:
    data = f.read().strip()

lines = data.split("\n")
lines = [l.split(" ") for l in lines]
nb_phrases = np.array([len(l) for l in lines])

# ========= TEST 1 =========
uniques = np.array([len(np.unique(l)) for l in lines])

print(f"Valid passphrases for test 1: {np.sum(uniques==nb_phrases)}/{len(lines)}")


# ========= TEST 2 =========
def sortString(str):
    return "".join(sorted(str))


sorted_lines = [[sortString(ll) for ll in l] for l in lines]
unique_sorted = np.array([len(np.unique(l)) for l in sorted_lines])

print(f"Valid passphrases for test 2: {np.sum(unique_sorted==nb_phrases)}/{len(lines)}")
