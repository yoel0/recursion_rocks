# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`
import random
# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"


def coin_flips(n):
    # Write code here
    if n <= 0:
        return []
    if n == 1:
        return ['H', 'T']
    combos = coin_flips(n - 1)
    print(n)
    return [x + 'H' for x in combos] + [x + 'T' for x in combos]


print(coin_flips(4))
print(coin_flips(1))

# print(coinFlips(2))
# => ["HH", "HT", "TH", "TT"]
