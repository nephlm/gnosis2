# -*- coding: utf-8 -*-
import random
import statistics

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
    samples = []
    for _ in range(num_rolls):
        result = roll(num_high_dice, num_med_dice, num_low_dice)
        total += result
        samples.append(result)
    stdev = statistics.stdev(samples)
    return ((total / num_rolls), stdev, iqr(samples))


def pain(num_pain_dice, num_rolls):
    die_sides = PAIN_DIE_SIDES
    total = 0.0
    samples = []
    for _ in range(num_rolls):
        select = [random.randint(1, die_sides) for x in range(num_pain_dice)]
        select.sort()
        select.reverse()
        roll = sum(select[:3])
        total += roll
        samples.append(roll)
    stdev = statistics.stdev(samples)
    return ((total / num_rolls), stdev, iqr(samples))


def iqr(samples):
    # inerquartile range - range of middle 50%
    samples.sort()
    q1 = samples[int(len(samples) * 0.25)]
    q2 = samples[int(len(samples) * 0.5)]
    q3 = samples[int(len(samples) * 0.75)]
    return q1, q2, q3


def cmp_key(element):
    return element[3]


if __name__ == "__main__":
    MAX_POOL = 4
    NUM_ROLLS = 5000
    results = []
    for num_high_dice in range(1, MAX_POOL + 1):
        for num_med_dice in range(1, MAX_POOL + 1):
            for num_low_dice in range(1, MAX_POOL + 1):
                mean, stdev, iqr_range = rolls(
                    num_high_dice, num_med_dice, num_low_dice, NUM_ROLLS
                )
                q1, median, q3 = iqr_range
                results.append(
                    (
                        num_high_dice,
                        num_med_dice,
                        num_low_dice,
                        mean,
                        stdev,
                        q1,
                        median,
                        q3,
                    )
                )

    for num_pain_dice in range(3, 3 * MAX_POOL + 1):
        mean, stdev, iqr_range = pain(num_pain_dice, NUM_ROLLS)
        q1, median, q3 = iqr_range
        results.append((0, num_pain_dice, 0, mean, stdev, q1, median, q3))

    results.sort(key=cmp_key)
    for k in results:
        print(
            f"| {k[0]} | {k[1]} | {k[2]} | {k[3]} | {k[4]:.3f} | {k[5]} | {k[6]} | {k[7]} | {'pain' if k[0] == 0 else ''} |"
        )
