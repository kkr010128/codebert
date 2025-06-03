import sys

A, B, C, K = list(map(int, input().split()))
ans = 0

if A > K:
    print(K)
    sys.exit()
ans += A
K -= A
if B > K:
    print(ans)
    sys.exit()
K -= B
if C > K:
    print(ans - K)
    sys.exit()
else:
    print(ans - C)