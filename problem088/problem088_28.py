n = int(input())
a = list(map(int, input().split()))
ans = 0
tmp = a[0]
for i in range(1,n):
    tmp = max(a[i], tmp)
    ans += tmp - a[i]
print(ans)