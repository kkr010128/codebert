import sys

N, R = map(int, sys.stdin.buffer.read().split())
rate = R

if N < 10:
  rate += 100 * (10 - N)

print(rate)
