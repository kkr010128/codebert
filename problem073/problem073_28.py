import sys
readline=sys.stdin.readline

N=int(readline())
# 1～(N - 1)の約数を数える

ans = 0
for i in range(1, N):
  for j in range(i, N, i):
    ans += 1

print(ans)
