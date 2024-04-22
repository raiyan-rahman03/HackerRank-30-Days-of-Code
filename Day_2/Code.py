#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#


def solve(meal_cost, tip_percent, tax_percent):
    a = float(meal_cost)  # Convert to float to allow for decimal values
    b = float(tip_percent)
    c = float(tax_percent)

    tip = a * b / 100
    tax = a * c / 100
    total = tip + tax + a

    return round(total)
    # Write your code here


if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    print(solve(meal_cost, tip_percent, tax_percent))
