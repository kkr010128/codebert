from time import time
from random import random

limit_secs = 2
start_time = time()

D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]

def calc_score(t):
    score = 0
    S = 0
    last = [-1] * 26
    for d in range(len(t)):
        S += s[d][t[d]]
        last[t[d]] = d
        for i in range(26):
            S -= c[i] * (d - last[i])
        score += max(10 ** 6 + S, 0)
    return score

def solution1():
    return [i % 26 for i in range(D)]

def solution2():
    t = None
    score = -1
    for i in range(26):
        nt = [(i + j) % 26 for j in range(D)]
        if calc_score(nt) > score:
            t = nt
    return t

def solution3():
    t = []
    for _ in range(D):
        score = -1
        best = -1
        t.append(0)
        for i in range(26):
            t[-1] = i
            new_score = calc_score(t)
            if new_score > score:
                best = i
                score = new_score
        t[-1] = best
    return t

def optimize0(t):
    return t

def optimize1(t):
    score = calc_score(t)
    while time() - start_time + 0.15 < limit_secs:
        d = int(random() * D)
        q = int(random() * 26)
        old = t[d]
        t[d] = q
        new_score = calc_score(t)
        if new_score < score:
            t[d] = old
        else:
            score = new_score
    return t

t = solution3()
t = optimize0(t)
print('\n'.join(str(e + 1) for e in t))
