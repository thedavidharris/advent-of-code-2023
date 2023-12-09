#!/usr/bin/env python3
from aocd import get_data
from itertools import pairwise
import re

data = get_data(day=9, year=2023)
# data = open('test.txt').read()

data = [[int(x) for x in line.split()] for line in data.splitlines()]

def run(line):
    diffs = [b-a for a,b in pairwise(line)]
    return line[-1] + run(diffs) if line else 0


print(f'Part 1: {sum(run(line) for line in data)}')
print(f'Part 2: {sum(run(line[::-1]) for line in data)}')