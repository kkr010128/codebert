n = int(input())
ans = 0
for i in range(1, n + 1):
    j = i
    while j <= n:
        ans += j
        j += i
print(ans)