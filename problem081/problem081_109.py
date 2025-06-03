#!/usr/bin/env python3

import sys

input = iter(sys.stdin.read().splitlines()).__next__

D, T, S = map(int, input().split())

print('Yes' if D <= T*S else 'No')

