# SOLUTION FOR DAY 12 OF 2024
# Riddle @ https://adventofcode.com/2024/day/12
# ============================

import numpy as np

input_path = "data/raw/2024/12.txt"
with open(input_path, "r") as f:
    data = f.read().strip().split("\n")


# ========= HELPERS =========
def get_perimeter(patch):
    raise NotImplementedError


def get_area(patch):
    raise NotImplementedError


def fence_price(area, perimeter):
    return area * perimeter


def alpha_to_num(alpha):
    return ord(alpha) - 64


# ========= TESTING DATA =========
example_data = [
    [
        "AAAA",
        "BBCD",
        "BBCC",
        "EEEC",
    ],
    [
        "OOOOO",
        "OXOXO",
        "OOOOO",
        "OXOXO",
        "OOOOO",
    ],
    [
        "RRRRIICCFF",
        "RRRRIICCCF",
        "VVRRRCCFFF",
        "VVRCCCJFFF",
        "VVVVCJJCFE",
        "VVIVCCJJEE",
        "VVIIICJJEE",
        "MIIIIIJJEE",
        "MIIISIJEEE",
        "MMMISSJEEE",
    ],
]


# ========= TEST 1 =========
def test1(data):
    assert len(set([len(x) for x in data])) == 1, "All patches must have the same size"
    map = {x: alpha_to_num(x) for x in set([y for x in data for y in x])}
    flat = np.array(data).flatten()
    plants_used = set([x for x in data])
    print(data, flat, plants_used)

    return None


assert test1(example_data[0]) == 140
assert test1(example_data[1]) == 772
assert test1(example_data[2]) == 1930
print(f"Solution for d12/t1: {test1(data)}")


# ========= TEST 2 =========
def test2(data):
    return None


assert test2(example_data) == -1
print(f"Solution for d12/t2: {test2(data)}")
