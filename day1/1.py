from aocd import get_data
import re

data = get_data(day=1, year=2023).strip()

# Part 1
def calibration(input):
    return sum(int(x[0]+x[-1]) for x in [re.findall(r"\d", l) for l in input.split("\n")])

print(f'Part 1: {calibration(data)}')

# Part 2
for s in "one two three four five six seven eight nine".split(): d=data.replace(s,s+str(len(s))+s)

print(f'Part 2: {calibration(d)}')