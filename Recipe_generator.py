import csv
import random

fname = "Recipes.csv"


def pick_one():
    with open(fname) as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))

    print()
    print(chosen_row)
    print()


pick_one()
