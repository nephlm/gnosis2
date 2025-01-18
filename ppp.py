# -*- coding: utf-8 -*-
import random

HIGH_DIE_SIDES = 12
MED_DIE_SIDES = 10
LOW_DIE_SIDES = 8
# HIGH_DIE_SIDES = 8
# MED_DIE_SIDES = 6
# LOW_DIE_SIDES = 4
PAIN_DIE_SIDES = MED_DIE_SIDES


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


def rolls(num_high_dice, num_med_dice, num_low_dice, num_rolls):
    total = 0.0
    for _ in range(num_rolls):
        total += roll(num_high_dice, num_med_dice, num_low_dice)
    return total / num_rolls


def pain(num_pain_dice, num_rolls):
    die_sides = PAIN_DIE_SIDES
    total = 0.0
    for _ in range(num_rolls):
        select = [random.randint(1, die_sides) for x in range(num_pain_dice)]
        select.sort()
        select.reverse()
        total += sum(select[:3])
    return total / num_rolls


def cmp_key(element):
    return element[3]


if __name__ == "__main__":
    MAX_POOL = 5
    NUM_ROLLS = 1000
    results = []
    for num_high_dice in range(1, MAX_POOL + 1):
        for num_med_dice in range(1, MAX_POOL + 1):
            for num_low_dice in range(1, MAX_POOL + 1):
                results.append(
                    (
                        num_high_dice,
                        num_med_dice,
                        num_low_dice,
                        rolls(num_high_dice, num_med_dice, num_low_dice, NUM_ROLLS),
                    )
                )

    for num_pain_dice in range(3, 3 * MAX_POOL + 1):
        results.append((0, num_pain_dice, 0, pain(num_pain_dice, NUM_ROLLS)))

    results.sort(key=cmp_key)
    for k in results:
        print(f"{k[0]}, {k[1]}, {k[2]}, {k[3]} {'pain' if k[0] == 0 else ''}")
