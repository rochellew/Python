# Calculates the probablity of there being a streak of 6 'heads' or 'tails' values

import random
numberOfStreaks = 0
EXPERIMENTRANGE = 10000
for experimentNumber in range(EXPERIMENTRANGE):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinResults = []
    for i in range(101):
        coinResults.append(random.randint(0,1))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    current = coinResults[0]
    next = coinResults[coinResults.index(current) + 1]
    tally = 0

    for result in coinResults:
        if current == next:
            tally += 1
            if tally >= 6:
                numberOfStreaks += 1
        current = coinResults[coinResults.index(current) + 1]
        next = coinResults[coinResults.index(current) + 1]

print(f'Number of streaks: {numberOfStreaks}')
print(f'Chance of streak: {(numberOfStreaks / EXPERIMENTRANGE)}%')
