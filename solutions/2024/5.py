# SOLUTION FOR DAY 5 OF 2024
# Riddle @ https://adventofcode.com/2024/day/5
# ============================

import numpy as np

input_path = "data/raw/2024/5.txt"
with open(input_path, "r") as f:
    data = f.read().strip().split("\n")


# ========= HELPERS =========
def parser(data):
    order = {int(x): int(y) for x, y in (pair.split("|") for pair in data if "|" in pair)}
    updates = [[int(y) for y in x.split(",")] for x in data if "," in x]
    correct_updates = f(order, updates)
    print(correct_updates)
    middle_nums = [x[len(x) // 2] for x in correct_updates]

    return sum(middle_nums)


def check(order, a, b):
    return order[a] == b


def f(order, updates):
    correct_updates = []
    for update in updates:
        correct = True
        for i in range(len(update) - 1):
            for j in range(i + 1, len(update) - 1):
                if order.get(update[i]) == update[j]:
                    correct = False
                    break
        if correct:
            correct_updates.append(update)
    return correct_updates


# ========= TESTING DATA =========
example_data = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",
    "",
    "75,47,61,53,29",
    "97,61,53,29,13",
    "75,29,13",
    "75,97,47,61,53",
    "61,13,29",
    "97,13,75,29,47",
]


# ========= TEST 1 =========
def test1(data):
    d = parser(data)
    return d


assert test1(example_data) == 143, f"Expected 143, but got {test1(example_data)}"
# print(f"Solution for d1/t1: {test1(data)}")


# ========= TEST 2 =========
def test2(data):
    return None


assert test2(example_data) == -1
print(f"Solution for d1/t2: {test2(data)}")
