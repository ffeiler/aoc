# SOLUTION FOR DAY 5 OF 2017
# Riddle @ https://adventofcode.com/2017/day/5
# ============================

import numpy as np

input_path = "data/raw/2017/5.txt"
with open(input_path, "r") as f:
    data = f.read().strip()


def lines_to_instructions(data):
    instructions = data.split("\n")
    instructions = [int(i) for i in instructions]
    return instructions


# ========= TEST 1 =========
def test1(instructions):
    pos = 0
    steps = 0
    while 0 <= pos <= len(instructions) - 1:
        pos_old = pos
        pos = pos_old + instructions[pos_old]
        instructions[pos_old] += 1
        steps += 1
    return steps


# ========= TEST 2 =========
def test2(instructions):
    pos = 0
    steps = 0
    while 0 <= pos <= len(instructions) - 1:
        pos_old = pos
        pos = pos_old + instructions[pos_old]
        if instructions[pos_old] >= 3:
            instructions[pos_old] -= 1
        else:
            instructions[pos_old] += 1
        steps += 1
    return steps


test_data = "0\n3\n0\n1\n-3"

assert test1(lines_to_instructions(test_data)) == 5
print(f"Test 1: Exit reached in {test1(lines_to_instructions(data))} steps")

assert test2(lines_to_instructions(test_data)) == 10
print(f"Test 2: Exit reached in {test2(lines_to_instructions(data))} steps")
