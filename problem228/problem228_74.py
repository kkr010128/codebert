import os, sys, re, math

memo = {}
def attack(h):
    result = memo.get(h)
    if result:
        return result

    result = 1
    if h > 1:
        result += attack(h // 2) * 2
    memo[h] = result
    return result

print(attack(int(input())))
