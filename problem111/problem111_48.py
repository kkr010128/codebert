n = int(input())
a = list(map(int,input().split()))
a.sort()
a.insert(0,0)
ans = 0
z = a[-1]
for i in range(1,n):
    ans += a[n - (i // 2)]
print(ans)