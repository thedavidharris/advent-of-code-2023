#!/usr/bin/env python3
from aocd import get_data

# Get data for day 10, year 2023
data = get_data(day=10, year=2023)
data = data.splitlines()

# Dictionary for possible movements from each pipe segment
directions = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'F': [(1, 0), (0, 1)],
    'S': [(-1, 0), (0, -1), (0, 1), (1, 0)]
}

# Find the starting position 'S'
start = next(((i, j) for i, row in enumerate(data) for j, cell in enumerate(row) if cell == 'S'), None)
assert start is not None, "Start position 'S' not found in the data."

# Initialize the current position and previous position
current_position = start
previous_position = None
area = 0
count = 1

# Loop until we get back to the start
while current_position != start or count == 1:
    x, y = current_position
    item = data[x][y]

    # Skip empty cells
    if item == '.':
        continue

    # Find the next position to move to, excluding the previous position
    for dx, dy in directions[item]:
        next_position = (x + dx, y + dy)
        # Check if the next position is valid and not the previous position
        if (0 <= next_position[0] < len(data) and
                0 <= next_position[1] < len(data[0]) and
                next_position != previous_position):
            previous_position, current_position = current_position, next_position
            area += y * dx
            break
    count += 1

print(f'Part 1: {(count - 1) // 2}')
print(f'Part 2: {area - count // 2 + 1}')