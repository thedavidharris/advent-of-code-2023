from aocd import get_data
import re

data = get_data(day=1, year=2023)

# Part 1
def calibration(input):
    return sum(int(digits[0] + digits[-1]) for line in input if (digits := re.findall(r'\d', line)))

print(f'Part 1: {calibration(data.splitlines())}')

# Part 2

sanitized_data = (
    data.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    ).splitlines()

print(f'Part 2: {calibration(sanitized_data)}')