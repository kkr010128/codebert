import sys
readline = sys.stdin.buffer.readline
h1, m1, h2, m2, k = map(int, readline().split())
print(60 * (h2 - h1) + m2 - m1 - k)