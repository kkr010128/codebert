import sys
N,M = map(int,input().split())
array = list(map(int,input().split()))

if not ( 1 <= N <= 10 ** 6 and 1 <= M <= 10 ** 4 ): sys.exit()
if not ( 1 <= min(array) and max(array) <= 10 ** 4 ): sys.exit()

ans = N - sum(array)

print(ans) if ans >= 0 else print(-1)