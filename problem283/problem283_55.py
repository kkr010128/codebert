#!/usr/bin/env python3

n = int(input())
print(int((n - 1) / 2) if n % 2 == 1 else int(n / 2) - 1)
