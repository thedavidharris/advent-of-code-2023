#!/usr/bin/env python3
from aocd import get_data
from math import prod

calculate_winning_ways = lambda t, d: sum(1 for s in range(t + 1) if (t - s) * s > d)

data = get_data(day=6, year=2023)
race_times, race_distances = (list(map(int, l.split()[1:])) for l in data.splitlines())

part1_ways = prod(calculate_winning_ways(t, d) for t, d in zip(race_times, race_distances))
part2_ways = calculate_winning_ways(int(''.join(map(str, race_times))), int(''.join(map(str, race_distances))))

print(f'Part 1: {part1_ways}')
print(f'Part 2: {part2_ways}')