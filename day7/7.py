#!/usr/bin/env python3
from aocd import get_data
from collections import Counter
from enum import Enum

input_data = get_data(day=7, year=2023)
# input_data = open('test.txt').read()

class HandType(Enum):
    FIVE_OF_KIND = 7
    FOUR_OF_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

# Define the function to determine the type of a poker hand
def hand_type(hand):
    c = Counter(hand)

    # Remove jokers from the hand and store their count
    jokers = c.pop("X", 0)
    # If there are no jokers or less than 5, sort the counts of the remaining cards
    counts = sorted(c.values()) if jokers < 5 else [0]

    # Add the jokers to the most common card count
    if counts:
        counts[-1] += jokers

    match counts:
        case *_, 5:
            return HandType.FIVE_OF_KIND
        case *_, 4:
            return HandType.FOUR_OF_KIND
        case *_, 2, 3:
            return HandType.FULL_HOUSE
        case *_, 3:
            return HandType.THREE_OF_KIND
        case *_, 2, 2:
            return HandType.TWO_PAIR
        case *_, 2:
            return HandType.ONE_PAIR
    return HandType.HIGH_CARD  # High card

# Define the solve function to process the data and calculate the score
def solve(data):
    plays = [line.split() for line in data.split("\n")]
    total_score = 0
    sorted_hands = sorted(
        (hand_type(hand), *map("X23456789TJQKA".index, hand), int(bid))
        for hand, bid in plays
    )
    for rank, (*_, bid) in enumerate(sorted_hands, start=1):
        score = rank * bid
        total_score += score
    return total_score

print(f'Part 1: {solve(input_data)}')
print(f'Part 2: {solve(input_data.replace("J", "X"))}')
