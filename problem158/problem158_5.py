#!/usr/bin/env python3
k, a, b = map(int, open(0).read().split())
print("NOGK"[b // k > (a - 1) // k::2])
