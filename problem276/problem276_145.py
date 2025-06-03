n = int(input())
a = list(map(int, input().split()))

ans = sum(a)
ans2 = 0
for i in range(n):
    if abs((ans - a[i]) - (ans2 + a[i])) < abs(ans - ans2):
        ans2 += a[i]
        ans -= a[i]
    else:
        break

print(abs(ans - ans2))
    
