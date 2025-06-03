import sys
N, M = [int(x) for x in input().split()]

s = 1
e = 2 * -(-M // 2)
for _ in range(M):
    if s >= e:
        s = N - 2 * (M // 2)
        e = N
    print(s, e)
    s += 1
    e -= 1