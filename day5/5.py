#!/usr/bin/env python3
import re
from aocd import get_data

# Retrieve data from Advent of Code (or from a file for testing)
data = get_data(day=5, year=2023)
# data = open('test.txt').read()

# Parse the input data into seed list and mapping lists
seed_input, *mapping_sections = data.split('\n\n')
initial_seeds = list(map(int, re.findall(r'\d+', seed_input)))
conversion_maps = [[list(map(int, line.split())) for line in section.splitlines()[1:]] 
                   for section in mapping_sections]

# Part 1 - Convert initial seed numbers through each mapping
current_seeds = initial_seeds
for conversion_map in conversion_maps:
    new_seeds = []
    for seed in current_seeds:
        converted_seed = seed  # Default to the same seed if no conversion is found
        for destination, source, length in conversion_map:
            if source <= seed < source + length:
                converted_seed = seed - source + destination
                break  # No need to check other rules once a match is found
        new_seeds.append(converted_seed)
    current_seeds = new_seeds
print(min(current_seeds))

# Part 2 - Convert ranges of seed numbers through each mapping
seed_ranges = [(initial_seeds[i], initial_seeds[i] + initial_seeds[i + 1]) 
               for i in range(0, len(initial_seeds), 2)]

for conversion_map in conversion_maps:
    new_seed_ranges = []
    while seed_ranges:
        start, end = seed_ranges.pop()
        for destination, source, length in conversion_map:
            overlap_start = max(start, source)
            overlap_end = min(end, source + length)
            if overlap_start < overlap_end:
                new_seed_ranges.append((overlap_start - source + destination, 
                                        overlap_end - source + destination))
                if overlap_start > start:
                    seed_ranges.append((start, overlap_start))
                if overlap_end < end:
                    seed_ranges.append((overlap_end, end))
                break
        else:
            new_seed_ranges.append((start, end))
    seed_ranges = new_seed_ranges

# Find the minimum starting location from the final list of seed ranges
min_location = min(start for start, _ in seed_ranges)
print(min_location)