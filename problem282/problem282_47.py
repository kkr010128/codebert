import sys
input = sys.stdin.readline

N, T = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
AB.sort()
dp0 = [0] * T # finish eating by time j
dp1 = [0] * T # order by time j
for A, B in AB:
    for j in range(T):
        dp1[j] = max(dp1[j], dp0[j] + B)
    for j in range(A, T)[::-1]:
        dp0[j] = max(dp0[j], dp0[j-A] + B)
print(dp1[-1])