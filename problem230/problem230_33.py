# coding: utf-8
import sys
from collections import deque

readline = sys.stdin.readline
sr = lambda: readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 左からgreedyに
N, D, A = lr()
monsters = []
for _ in range(N):
    x, h = lr()
    monsters.append((x, h))

monsters.sort()
bomb = deque()
answer = 0
attack = 0
for x, h in monsters:
    while bomb:
        if bomb[0][0] + D < x:
            attack -= bomb[0][1]
            bomb.popleft()
        else:
            break
    h -= attack
    if h > 0:
        t = -(-h//A)
        answer += t
        bomb.append((x + D, A * t))
        attack += A * t

print(answer)
