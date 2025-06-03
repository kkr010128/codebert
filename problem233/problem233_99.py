n = int(input())
P = list(map(int, input().split()))
ans = 1
x = P[0]
for p in P:
    if x > p:
        ans += 1
        x = p
print(ans)