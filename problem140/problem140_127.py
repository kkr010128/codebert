#!/usr/bin/env python3

T = list(input())

cnt = 0
for i in range(len(T)):
    if T[i] == '?':
        T[i] = 'D'

print(''.join(T))
