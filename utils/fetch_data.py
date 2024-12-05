import os
import time

import requests


def fetch_data(y, d):
    assert y >= 2015
    assert 1 <= d <= 25
    month_now = time.localtime().tm_mon
    assert month_now == 12, "It's not December yet!"

    base_path = "https://adventofcode.com/"
    url = base_path + str(y) + "/day/" + str(d) + "/input"
    out_fn = "data/raw/" + str(y) + "/" + str(d) + ".txt"

    if os.path.exists(out_fn):
        return  # already fetched
    else:
        os.makedirs(os.path.dirname(out_fn), exist_ok=True)

    token = open("SESSION_TOKEN.txt").read().strip()
    cookies = {"session": token}

    r = requests.get(url, cookies=cookies)
    if r.status_code == 200:
        with open(out_fn, "w") as f:
            f.write(r.text)
        print(f"Fetched {d}/{y}")
    else:
        print("Error fetching data")


def fetch_historical_data(y_now=2023):
    """Fetch raw data for all days of all years from 2015 on"""
    for y in range(2015, y_now):
        for d in range(1, 26):
            fetch_data(y, d)


def make_root_dirs(y_now):
    os.makedirs("data/", exist_ok=True)
    os.makedirs("data/raw/", exist_ok=True)
    os.makedirs("data/processed/", exist_ok=True)
    os.makedirs("solutions/", exist_ok=True)
    for y in range(2015, y_now + 1):
        os.makedirs(f"data/raw/{y}/", exist_ok=True)
        os.makedirs(f"data/processed/{y}/", exist_ok=True)
        os.makedirs(f"solutions/{y}/", exist_ok=True)


def create_empty_solutions(y_now=2023):
    for y in range(2015, y_now + 1):
        for d in range(1, 26):
            fn = f"solutions/{y}/{d}.py"
            if not os.path.exists(fn):
                with open(fn, "w") as f:
                    f.write(f"# SOLUTION FOR DAY {d} OF {y}\n")
                    f.write(f"# Riddle @ https://adventofcode.com/{y}/day/{d}\n")
                    f.write("# ============================\n\n")
                    f.write("import numpy as np\n")
                    f.write("\n\n")
                    f.write(f"input_path = 'data/raw/{y}/{d}.txt'\n")
                    f.write("with open(input_path, 'r') as f:\n")
                    f.write("    data = f.read().strip().split('\t')\n")

                    f.write("\n\n")
                    f.write("# ========= HELPERS =========\n")
                    f.write("def helper(data):\n")
                    f.write("    return data\n")

                    f.write("\n\n")
                    f.write("# ========= TESTING DATA =========\n")
                    f.write("example_data = None\n")

                    f.write("\n\n")
                    f.write("# ========= TEST 1 =========\n")
                    f.write("def test1(data):\n")
                    f.write("    return None\n")
                    f.write("\n")
                    f.write("assert test1(example_data) == -1\n")
                    f.write(f'print(f"Solution for d{d}/t1: {{test1(data)}}")\n')

                    f.write("\n\n")
                    f.write("# ========= TEST 2 =========\n")
                    f.write("def test2(data):\n")
                    f.write("    return None\n")
                    f.write("\n")
                    f.write("assert test2(example_data) == -1\n")
                    f.write(f'print(f"Solution for d{d}/t2: {{test2(data)}}")\n')
