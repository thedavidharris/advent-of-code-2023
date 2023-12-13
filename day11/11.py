#!/usr/bin/env python3
from aocd import get_data

# Get data for day 10, year 2023
data = get_data(day=11, year=2023).splitlines()

coordinates = []
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == '#':
            coordinates.append((x, y))

# Separate the x and y coordinates into two lists
xs, ys = zip(*coordinates)

def calculate_distance(points, l):
    # Transform points based on the presence of the point in the original set
    transformed_points = [sum((l, 1)[p in points] for p in range(point)) for point in points]
    # Calculate the sum of pairwise absolute differences
    total_distance = sum(abs(a - b) for a in transformed_points for b in transformed_points) // 2
    return total_distance

# Calculate and print the distance sums for the given scenarios
for l in (2, 1_000_000):
    x_distances_sum = calculate_distance(xs, l)
    y_distances_sum = calculate_distance(ys, l)
    print(x_distances_sum + y_distances_sum)