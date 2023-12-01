# SOLUTION FOR DAY 1 OF 2023
# Riddle @ https://adventofcode.com/2023/day/1
# ============================

input_path = "data/raw/2023/1.txt"
with open(input_path, "r") as f:
    data = f.read().strip().split("\n")

# ========= TESTING DATA =========
test_data_1 = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
test_data_2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]


# ========= HELPERS =========
def numbers_from_string(s):
    return [int(c) for c in s if c.isdigit()]


def numbers_from_list(l):
    return [numbers_from_string(s) for s in l]


def get_first_and_last_numbers(l):
    cal_nums = []
    for lof in l:
        first_num = lof[0]
        last_num = lof[-1]
        calibration_num = int(f"{first_num}{last_num}")
        cal_nums.append(calibration_num)
    return cal_nums


def replace_spelled_nums(data):
    ks = repl_alpha_nums.keys()
    d = data.copy()
    for k in ks:
        for i, l in enumerate(d):
            if k in l:
                repl = str(repl_alpha_nums[k])
                d[i] = l.replace(k, k[0] + repl + k[-1])
    return d


# ========= TEST 1 =========
def test1(data):
    nums_in_list = numbers_from_list(data)
    cal_vals = get_first_and_last_numbers(nums_in_list)
    sum_cal = sum(cal_vals)
    return sum_cal


assert test1(test_data_1) == 142, "Test data for first task is not correct!"
print(f"Solution for test1: {test1(data)}")


# ========= TEST 2 =========,
repl_alpha_nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def test2(data):
    l = replace_spelled_nums(data)
    nums_in_list = numbers_from_list(l)
    cal_vals = get_first_and_last_numbers(nums_in_list)
    sum_cal = sum(cal_vals)
    return sum_cal


assert (
    test2(test_data_2) == 281
), f"Test data for second task is not correct! {test2(test_data_2)}"
print(f"Solution for test2: {test2(data)}")
