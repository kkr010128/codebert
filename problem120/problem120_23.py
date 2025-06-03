#B問題
ans = 0
n, k = map(int, input().split())
P = list(map(int, input().split()))
for i in range(k):
    ans += min(P)
    P.remove(min(P))

print(ans)