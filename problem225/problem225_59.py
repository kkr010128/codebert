import sys

H, A = map(int, next(sys.stdin.buffer).split())
print(-(-H // A))