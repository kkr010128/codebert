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


n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

pidx, qidx = 0, 0
candidates = list(itertools.permutations(range(1, n+1), n))
for index, candidate in enumerate(candidates):
    candidate = list(candidate)

    if candidate == p:
        pidx = index
    if candidate == q:
        qidx = index

print(abs(pidx - qidx))
