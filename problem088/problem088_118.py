n = int(input())
a = list(map(int, input().split()))

ans = 0
maxi = 0
for i in range(n):
    if a[i] < maxi:
        ans += (maxi - a[i])
        a[i] = maxi
    maxi = max(maxi, a[i])


print(ans)
