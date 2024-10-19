# -*- coding: utf-8 -*-
import random

HIGH_DIE_SIDES = 12
MED_DIE_SIDES = 10
LOW_DIE_SIDES = 8
# HIGH_DIE_SIDES = 8
# MED_DIE_SIDES = 6
# LOW_DIE_SIDES = 4

PAIN_DIE_SIDES = MED_DIE_SIDES
# PAIN_DICE = 3

HIGH_ADVANTAGE = 3
MED_ADVANTAGE = 3
LOW_ADVANTAGE = 3

ITERATIONS = 1000

CRIT_THRESHOLD = 7
THRESHOLD = 1


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
    # num_pain_dice = 3
    for num_pain_dice in range(3, 12):
        results = {
            "crit_fail": 0,
            "fail": 0,
            "draw": 0,
            "success": 0,
            "crit_success": 0,
        }
        for _ in range(ITERATIONS):
            pc_roll = roll(HIGH_ADVANTAGE, MED_ADVANTAGE, LOW_ADVANTAGE)
            pain_roll = pain(num_pain_dice)
            if (pc_roll - pain_roll) < (CRIT_THRESHOLD * -1):
                results["crit_fail"] += 1
            elif (pc_roll - pain_roll) < (THRESHOLD * -1):
                results["fail"] += 1
            elif (pc_roll - pain_roll) < (THRESHOLD):
                results["draw"] += 1
            elif (pc_roll - pain_roll) < (CRIT_THRESHOLD):
                results["success"] += 1
            else:
                results["crit_success"] += 1
        print(f"{num_pain_dice=}")
        print({x: (y * 100 / ITERATIONS) for x, y in results.items()})


if __name__ == "__main__":
    main()
