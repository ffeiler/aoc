# SOLUTION FOR DAY 3 OF 2017
# Riddle @ https://adventofcode.com/2017/day/3
# ============================

import math

import numpy as np

input_path = "data/raw/2017/3.txt"


# ========= TEST 1 =========
def manhattan_dist(mid, cx, cy):
    d = abs(cx - mid) + abs(cy - mid)
    return d


# ========= TEST 2 =========
def sum_of_all_neighbours(m, cx, cy):
    neighbour_grid = m[cx - 1 : cx + 2, cy - 1 : cy + 2]
    return int(np.sum(neighbour_grid))


# ========= GENERAL =========
def get_next_op(last_op, m, cx, cy):
    order = ["r", "u", "l", "d"]
    ix_op = order.index(last_op)
    nix_op = (ix_op + 1) % len(order)
    try_op = order[nix_op]
    x, y = dcoord_from_op(try_op, cx, cy)

    if m[x, y] == 0:
        return try_op
    else:
        return last_op


def dcoord_from_op(op, cx, cy):
    assert op in ["r", "u", "l", "d"]
    x, y = cx, cy
    if op == "r":
        x = cx + 1
    elif op == "u":
        y = cy + 1
    elif op == "l":
        x = cx - 1
    elif op == "d":
        y = cy - 1
    return x, y


def fill_current_cell(task, m, cx, cy, n):
    if task == "1":
        return n
    if task == "2":
        return sum_of_all_neighbours(m, cx, cy)


def layout_grid(nb, task):
    nx = math.ceil(math.sqrt(nb))
    if nx % 2 == 0:
        nx += 1
    nx = max(nx, 3)
    if task == "2":
        nx = 3 * nx
    ny = nx
    mid = nx // 2

    m = np.zeros((nx, ny))

    cx, cy = mid, mid
    m[cx, cy] = 1

    op = "r"
    for n in range(2, nb + 1):
        op = get_next_op(op, m, cx, cy)
        cx, cy = dcoord_from_op(op, cx, cy)
        m[cx, cy] = fill_current_cell(task, m, cx, cy, n)
    return m, mid


# ========= SOLUTIONS =========
def test1(nb):
    task = "1"
    grid, mid = layout_grid(nb, task)
    cx, cy = np.where(grid == nb)
    dm = manhattan_dist(mid, cx, cy)
    return dm


def test2(nb):
    task = "2"
    grid, mid = layout_grid(int(nb / 10), task)
    min_val = int(np.min(grid[np.where(grid > nb)]))
    return min_val


with open(input_path, "r") as f:
    data = f.read().strip()
data = int(data)
assert test1(1024) == 31
assert test1(23) == 2
assert test1(12) == 3
print(f"Answer for task 1: {test1(data)}")

print(f"Answer for test2: {test2(data)}")
