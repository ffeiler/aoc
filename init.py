import argparse
import os
import time

Y_NOW = int(time.localtime().tm_year)
D_NOW = int(time.localtime().tm_mday)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--historical", action="store_true")

    return parser.parse_args()


from utils.fetch_data import (
    create_empty_solutions,
    fetch_data,
    fetch_historical_data,
    make_root_dirs,
)

if __name__ == "__main__":
    make_root_dirs(Y_NOW)
    args = parse_args()
    if args.historical:
        fetch_historical_data(Y_NOW)
    else:
        print(f"Fetching data for {D_NOW}/{Y_NOW}")
        fetch_data(Y_NOW, D_NOW)

    create_empty_solutions(Y_NOW)
