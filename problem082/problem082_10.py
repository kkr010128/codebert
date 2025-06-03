import math
import itertools


# 与えられた数値の桁数と桁値の総和を計算する.
def calc_digit_sum(num):
    digits = sums = 0
    while num > 0:
        digits += 1
        sums += num % 10
        num //= 10
    return digits, sums


s = input()
t = input()

answer = len(t)
for index in range(len(s) - (len(t) - 1)):
    d = s[index:index+len(t)]
    match = 0
    for idx in range(len(t)):
        if t[idx] == d[idx]:
            match += 1

    answer = min(answer, len(t) - match)

print(answer)