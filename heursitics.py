# -*- coding: utf-8 -*-
import random

HIGH_DIE_SIDES = 12
MED_DIE_SIDES = 10
LOW_DIE_SIDES = 8
# HIGH_DIE_SIDES = 8
# MED_DIE_SIDES = 6
# LOW_DIE_SIDES = 4

PAIN_DIE_SIDES = MED_DIE_SIDES
PAIN_DICE = 3

HIGH_ADVANTAGE = 1
MED_ADVANTAGE = 1
LOW_ADVANTAGE = 1

ITERATIONS = 10000


def roll(num_high_dice, num_med_dice, num_low_dice):
    idx_dict = {0: HIGH_DIE_SIDES, 1: MED_DIE_SIDES, 2: LOW_DIE_SIDES}
    high_val = [0, 0, 0]
    num_rolls = (num_high_dice, num_med_dice, num_low_dice)
    for idx, sides in idx_dict.items():
        for _ in range(num_rolls[idx]):
            val = random.randint(1, sides)
            if high_val[idx] < val:
                high_val[idx] = val
    return high_val[0] + high_val[1] + high_val[2]


# def rolls(num_high_dice, num_med_dice, num_low_dice, num_rolls):
#     total = 0.0
#     for _ in range(num_rolls):
#         total += roll(num_high_dice, num_med_dice, num_low_dice)
#     return total / num_rolls


def pain(num_pain_dice):
    die_sides = PAIN_DIE_SIDES
    select = [random.randint(1, die_sides) for x in range(num_pain_dice)]
    select.sort()
    select.reverse()
    return sum(select[:3])


# def cmp_key(element):
#     return element[3]


def main():
    results = {}
    for i in range(3, 31):
        results[i] = 0

    for _ in range(ITERATIONS):
        total = pain(PAIN_DICE)
        results[total] += 1

    for idx, val in results.items():
        print(f"{idx}: {val}: {'*'*int(val*.5/(ITERATIONS/1000))}")

    results = {}
    for i in range(3, 31):
        results[i] = 0

    for _ in range(ITERATIONS):
        total = roll(HIGH_ADVANTAGE, MED_ADVANTAGE, LOW_ADVANTAGE)
        results[total] += 1

    for idx, val in results.items():
        print(f"{idx}: {val}: {'*'*int(val*.5/(ITERATIONS/1000))}")


if __name__ == "__main__":
    main()
