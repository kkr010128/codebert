import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

ans = 0
for i in range(N):
    if i % 2 == 0 and A[i] % 2 == 1:
        ans += 1

print(ans)