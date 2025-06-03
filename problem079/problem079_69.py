s = int(input())

a = []

a.append(1)
a.append(0)
a.append(0)
for i in range(3,s+1):
    a.append(sum(a)-a[i-1]-a[i-2])

ans = a[-1] % (10**9 + 7)

print(ans)