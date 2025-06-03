n = int(input())
p = list(map(int, input().split()))
minp = 2*10**5
ans = 0
for i in range(n):
    if minp >= p[i]:
        minp = p[i]
        ans += 1
print(ans)