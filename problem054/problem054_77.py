from sys import stdin
from itertools import product

suits = ['S', 'H', 'C', 'D']
suits_priority = {
    'S': 1,
    'H': 2,
    'C': 3,
    'D': 4
}
ranks = list(range(1, 14))

original_deck = set(product(suits, ranks))

if __name__ == '__main__':
    n = int(stdin.readline().rstrip())
    deck = set()
    for _ in range(n):
        suit, rank = stdin.readline().rstrip().split()
        deck.add((suit, int(rank)))

    diff = list(original_deck - deck)
    diff.sort(key=lambda x: x[1])
    diff.sort(key=lambda x: suits_priority[x[0]])

    for card in diff:
        print("{} {}".format(*card))

