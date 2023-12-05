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
# Check each line for numbers
for y, line in enumerate(data):
    for match in re.finditer(r"\d+", line):
        num = int(match.group())
        x_start, x_end = match.start(), match.end() - 1  # x_end is inclusive
        found_symbol = False

        # Check if the number is adjacent to a symbol
        for x in range(x_start, x_end + 1):
            # Define the adjacent positions (including diagonals)
            adjacent_positions = [
                (x, y), (x - 1, y), (x + 1, y),  # Current, left, and right
                (x, y - 1), (x - 1, y - 1), (x + 1, y - 1),  # Above
                (x, y + 1), (x - 1, y + 1), (x + 1, y + 1)  # Below
            ]
            for adj_x, adj_y in adjacent_positions:
                if (adj_x, adj_y) in symbols:
                    parts_sum += num  # Add to sum if adjacent to any symbol
                    if symbols[(adj_x, adj_y)] == '*':
                        gears[(adj_x, adj_y)].append(num)  # Add to gears if adjacent to a gear
                    found_symbol = True
                    break  # Break the inner loop if we found a symbol

            if found_symbol:
                break  # Break the outer loop if we found a symbol

# ========= PART 1 =========
print(f'Part 1: {parts_sum}')

# ========= PART 2 =========
print(f'Part 2: {sum(prod(part_nums) for part_nums in gears.values() if len(part_nums) == 2)}')