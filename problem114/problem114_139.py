#!/usr/bin/env python3

D = int(input())
C = list(map(int, input().split()))
S = [list(map(int, input().split())) for i in range(D)]
T = [int(input())-1 for i in range(D)] #B

last = {}
for i in range(26):
    last[i] = -1

s = 0
for d in range(D):
    last[T[d]] = d
    s += S[d][T[d]]
    for i in range(26):
        #print(d-last[i])
        s -= C[i] * (d-last[i])
    print(s)
