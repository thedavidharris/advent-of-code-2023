#!/usr/bin/env python3

from aocd import get_data
import re
from math import prod
from collections import defaultdict

def is_symbol(x):
    return x != '.' and not x.isdigit()

data = get_data(day=3, year=2023)

data = data.splitlines()

# Get map of Symbols
symbols = {(x, y): c for y, line in enumerate(data) for x, c in enumerate(line) if is_symbol(c)}

gears = defaultdict(list)
parts_sum = 0
for y, line in enumerate(data):
    for match in re.finditer(r"\d+", line):
        num = int(match.group())
        for (symbol_x, symbol_y), c in symbols.items():
            if (match.start() - 1 <= symbol_x <= match.end()) and (y - 1 <= symbol_y <= y + 1):
                parts_sum += num
                if c == "*":
                    gears[(symbol_x, symbol_y)].append(num)
                break

print(f'Part 1: {parts_sum}')

print(f'Part 2: {sum(prod(part_nums) for part_nums in gears.values() if len(part_nums) == 2)}')