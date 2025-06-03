n = int(input())
p = list(map(int, input().split()))
m = p[0]
ans = 0
for i in p:
    if (m >= i):
        ans += 1
    m = min(i,m)
print(ans)