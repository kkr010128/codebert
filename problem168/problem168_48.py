N, M = map(int, input().split())
Alst = list(map(int, input().split()))
k = sum(Alst)
ans = N - k
if ans >= 0:
    print(ans)
else:
    print(-1)