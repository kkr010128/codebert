#!/usr/bin/env python3
N, A, B = [int(str) for str in input().strip().split()]

if (B - A) % 2:
    left = A + (B - A) // 2
    right = N - (B - A) // 2 - A
    print(min(left, right))
else:
    print((B - A) // 2)