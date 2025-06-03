#!/usr/bin/env python3
a, b, c = map(int, input().split())
print("YNeos"[c - a - b < 0 or 0 <= 4 * a * b - (a + b - c)**2::2])
