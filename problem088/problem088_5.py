n = int(input())
a = list(map(int,input().split()))

max_num = a[0]
ans = 0
for i in range(1,n):
    max_num = max(max_num, a[i])
    if max_num != a[i]:
        ans += (max_num - a[i])
print(ans)