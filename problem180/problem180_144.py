import sys
n, k = map(int, sys.stdin.buffer.read().split())
rem = n % k
print(min(rem, k - rem))