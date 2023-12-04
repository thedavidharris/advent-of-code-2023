#!/usr/bin/env python3

from aocd import get_data
import re
import math
from collections import defaultdict 

data = get_data(day=2, year=2023)
# data = open('test.txt').read()

data = [re.split('; |: ', x)[1:] for x in data.strip().splitlines()]

# Part 1

max_values = {
    'red': 12,
    'green': 13,
    'blue': 14
}

valid_sum = 0
for game_id, game in enumerate(data,1):
    if all(int(number) <= max_values[color] for pull in game for number, color in(re.findall(r'(\d+) (\w+)', pull))):
        valid_sum += game_id

print(f'Part 1: {valid_sum}')

# Part 2

product_sums = 0
for game in data:
    minimum_values = defaultdict(int)
    for pull in game:
        for value, color in re.findall(r'(\d+) (\w+)', pull):
            minimum_values[color] = max(minimum_values[color], int(value))
    product_sums += math.prod(minimum_values.values())

print(f'Part 2: {product_sums}')