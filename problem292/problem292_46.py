#!/usr/bin/env python3
N = int(input())
D = [int(s) for s in input().split()]

life = 0

for i in range(N):
    for j in range(i+1, N):
        life += D[i] * D[j]

print(life)
