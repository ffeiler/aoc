# SOLUTION FOR DAY 2 OF 2023
# Riddle @ https://adventofcode.com/2023/day/2
# ============================

import numpy as np

input_path = "data/raw/2023/2.txt"
with open(input_path, "r") as f:
    data = f.read().strip().split("\n")


# ========= TESTING DATA =========
test_data_1 = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]
condition_test = [12, 13, 14]

# ========= HELPERS =========
COLORS = ["red", "green", "blue"]


class Game:
    def __init__(self, g, condition=None):
        self.game_string = g
        self.game_id = None
        self.reds = []
        self.blues = []
        self.greens = []
        sets = self.game_string.split(":")[1].split(";")
        self.sets = [s.strip(" ") for s in sets]

        self.parse_game()
        self.valid = False if condition is None else self.is_valid(condition)
        self.power = np.prod([max(self.reds), max(self.greens), max(self.blues)])

    def parse_game(self):
        self.game_id = self.get_game_id(self.game_string)
        for s in self.sets:
            self.reds.append(self.count_balls(s, "red"))
            self.blues.append(self.count_balls(s, "blue"))
            self.greens.append(self.count_balls(s, "green"))

    def get_game_id(self, s):
        return int(s.split(":")[0].split(" ")[1])

    def count_balls(self, s, c):
        num_color = 0
        draws = s.split(", ")
        for d in draws:
            if c in d:
                num_color = int(d.split(" ")[0])
        return num_color

    def is_valid(self, condition: list):
        r, g, b = condition
        if r < max(self.reds):
            return False
        elif g < max(self.greens):
            return False
        elif b < max(self.blues):
            return False
        else:
            return True

    def __repr__(self) -> str:
        return f"Game {self.game_id}: {self.reds} red, {self.greens} green, {self.blues} blue -  is valid: {self.valid}, power: {self.power}"


# ========= PART 1 =========
def test1(data, condition):
    ids_valid = []
    for l in data:
        g = Game(l, condition=condition)
        if g.valid:
            ids_valid.append(g.game_id)

    return sum(ids_valid)


assert test1(test_data_1, condition_test) == 8
print(f"Solution for part 1: {test1(data, condition_test)}")


# ========= PART 2 =========
def test2(data):
    ps = []
    for l in data:
        g = Game(l)
        ps.append(g.power)

    return sum(ps)


assert test2(test_data_1) == 2286
print(f"Solution for part 2: {test2(data)}")
