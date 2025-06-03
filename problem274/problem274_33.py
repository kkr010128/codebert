# AtCoder Beginner Contest 146
# F - Sugoroku
# https://atcoder.jp/contests/abc146/tasks/abc146_f
import sys
N, M = map(int, input().split())
*S, = map(int, input())
S.reverse()

i = 0
ans = []
while i < N:
    for m in range(M, 0, -1):
        if i+m <= N and S[i+m] == 0:
            i += m
            ans += [m]
            break
    else:
        print(-1)
        sys.exit()

print(*ans[::-1])
