#!/usr/bin/env python3
from aocd import get_data
from itertools import cycle
from math import lcm
import re

data = get_data(day=8, year=2023)
# data = open('test.txt').read()
# data = open('test2.txt').read()


directions, _, *ways_input = data.splitlines()

ways = {
    way[0]: 
        {
            'L': way[1], 
            'R': way[2]
        } 
    for way in [re.findall(r'\w+', x) for x in ways_input]
}

totals = []
for pos in [w for w in ways if w.endswith('A')]:
    c = cycle(directions)
    step = 0
    while not pos.endswith('Z'):
        step += 1
        pos = ways[pos][next(c)]
    totals.append(step)

print(f'Part 1: {totals[0]}')
print(f'Part 2: {lcm(*totals)}')