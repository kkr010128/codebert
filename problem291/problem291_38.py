#!/usr/bin/env python3
A, B = [int(s) for s in input().split()]
print(A - 2 * B if A - 2 * B > 0 else 0)
