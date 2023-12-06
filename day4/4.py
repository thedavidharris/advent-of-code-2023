#!/usr/bin/env python3

from aocd import get_data
import re
from math import pow
from collections import defaultdict

data = get_data(day=4, year=2023).splitlines()
# data = open('test.txt').read().splitlines()

total = 0
cards = defaultdict(int)
for i, line in enumerate(data):
    cards[i] += 1
    winning, has = map(set, (map(str.split, line.split('|'))))
    count = len(winning & has)
    if count > 0:
        total += 2**(count-1)
    for j in range(count):
        cards[i + j + 1] += cards[i]

print(f'Part1: {total}')

print(f'Part 2: {sum(cards.values())}')