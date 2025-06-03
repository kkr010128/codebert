#!/usr/bin/env python3
import math

n, m = map(int, input().split())

nans = (n * (n - 1)) // 2
mans = (m * (m - 1)) // 2

print(nans + mans)
