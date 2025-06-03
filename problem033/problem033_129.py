# Aizu Problem ITP_1_11_A: Dice I
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


def do_roll(dice, roll):
    d1, d2, d3, d4, d5, d6 = dice
    if roll == 'E':
        return [d4, d2, d1, d6, d5, d3]
    elif roll == 'W':
        return [d3, d2, d6, d1, d5, d4]
    elif roll == 'N':
        return [d2, d6, d3, d4, d1, d5]
    elif roll == 'S':
        return [d5, d1, d3, d4, d6, d2]
    else:
        assert False, "We should never reach this point!"
    

dice = [int(_) for _ in input().split()]
for roll in input().strip():
    dice = do_roll(dice, roll)

print(dice[0])