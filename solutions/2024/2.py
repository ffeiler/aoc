# SOLUTION FOR DAY 2 OF 2024
# Riddle @ https://adventofcode.com/2024/day/2
# ============================

import numpy as np

input_path = "data/raw/2024/2.txt"
with open(input_path, "r") as f:
    data = f.read().strip().split("\n")


# ========= HELPERS =========
def parse_data(data):
    levels = [x.split(" ") for x in data]
    levels_int = [[int(x) for x in lvl] for lvl in levels]
    return levels_int


def is_safe(report, remove_index=None):
    diffs = np.diff(report) if remove_index is None else np.diff(np.delete(report, remove_index))
    sign = np.sign(diffs[0])
    if sign == 0:
        return False
    allowed = [sign, 2 * sign, 3 * sign]
    all_allowed = all(d in allowed for d in diffs)
    all_same_sign = len(set(np.sign(diffs))) == 1
    safe = all_allowed and all_same_sign
    return safe


def dampener(report):
    for i in range(len(report)):
        if is_safe(report, i):
            return True
    return False


# ========= TESTING DATA =========
example_data = [
    "7 6 4 2 1",
    "1 2 7 8 9",
    "9 7 6 2 1",
    "1 3 2 4 5",
    "8 6 4 4 1",
    "1 3 6 7 9",
]


# # ========= TEST 1 =========
def test1(data):
    reports = parse_data(data)
    check = [is_safe(r) for r in reports]
    return sum(check)


assert test1(example_data) == 2
print(f"Solution for d2/t1: {test1(data)}")


# # ========= TEST 2 =========
def test2(data):
    reports = parse_data(data)
    check = [is_safe(r) for r in reports]
    unsafe_reports = [r for r, safe in zip(reports, check) if not safe]
    safe_by_dampener = [dampener(r) for r in unsafe_reports]
    return sum(check + safe_by_dampener)


assert test2(example_data) == 4
print(f"Solution for d2/t2: {test2(data)}")
