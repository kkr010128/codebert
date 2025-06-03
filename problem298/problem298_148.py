#!/usr/bin/env python3
N, K = [int(s) for s in input().split()]
h = [int(s) for s in input().split()]

print(len(list(filter(lambda x: x >= K, h))))