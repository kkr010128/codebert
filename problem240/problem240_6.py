import itertools
# import math

# N = int(input())
# S = input()
# n, *a = map(int, open(0))
N, M = map(int, input().split())
# P = list(map(int, input().split()))
# Q = list(map(int, input().split()))
# S = input()

aced = {}
waed = [0] * (N + 1)

cnt_ac = 0
for i in range(M):
    p_i, S_i = input().split()
    if S_i == 'WA':
        if not p_i in aced:
            waed[int(p_i)] += 1
    else:
        if not p_i in aced:
            cnt_ac += 1
            aced[p_i] = 1

cnt_pena = 0
for k in aced:
    cnt_pena += waed[int(k)]

print(cnt_ac, cnt_pena)
# print(aced)