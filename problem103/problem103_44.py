n = int(input())
a = list(map(int, input().split()))
ans = 1000
stock = 0
for i in range(n-1):
    if a[i+1] > a[i]:
        buy = ans//a[i]
        stock += buy
        ans -= buy*a[i]
    else:
        ans += stock*a[i]
        stock = 0

ans += stock*a[-1]
print(ans)
