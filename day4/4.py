#!/usr/bin/env python3

from aocd import get_data

data = get_data(day=4, year=2023).splitlines()
# data = open('test.txt').read().splitlines()

t=0
c=[1]*len(data)
for i, line in enumerate(data):
    winning, has = map(set, (map(str.split, line.split('|'))))
    count = len(winning & has)
    if count > 0:
        t += 2**(count-1)
    for j in range(count):
        c[i + j + 1] += c[i]

print(f'Part 1: {t}')

print(f'Part 2: {sum(c)}')