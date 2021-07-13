# Calculates the probablity of there being a streak of 6 'heads' or 'tails' values

import random

numberOfStreaks = 0
streak = 0
EXPERIMENT_RANGE = 10000
FLIPS_PER_EXPERIMENT = 100
for experimentNumber in range(EXPERIMENT_RANGE):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinResults = []
    for i in range(101):
        coinResults.append(random.randint(0, 1))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(1, len(coinResults)):
        if  coinResults[i] == coinResults[i-1]:
            streak += 1
        else:
            streak = 0
        if streak == 6:
            numberOfStreaks += 1

    coinResults = []

chance = numberOfStreaks /  (EXPERIMENT_RANGE * FLIPS_PER_EXPERIMENT)
chance_percent = round(chance * 100, 4)
print(f"Chance of streak: {chance_percent}%")
