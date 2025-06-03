import sys

read = sys.stdin.read
readline = sys.stdin.readline

H, M, h, m, K = map(int, read().split())

m -= M
h -= H
if m < 0:
    m += 60
    h -= 1

answer = h * 60 + m - K
print(answer)
