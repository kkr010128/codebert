n = int(input())

i = 1
ans = 0
while (i <= n):
    total = sum(j for j in range(i, n+1, i))
    ans += total
    i += 1
print(ans)