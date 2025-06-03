N = int(input())
P = list(map(int,input().split()))

ans = 1
min = P[0]
for i in P[1:]:
    if min >= i:
        ans += 1
        min = i
print(ans)
