n = int(input())
a = list(map(int,input().split()))
tmp = [0] * (n+1)
ans = 0
for i in range(n):
    tmp[a[i]] += 1
for i in range(1,len(tmp)):
    if tmp[i] > 1:
        ans += int(tmp[i] * (tmp[i] - 1) / 2)
for i in range(n):
    if tmp[a[i]] > 1:
        print(ans - int(tmp[a[i]] * (tmp[a[i]] - 1) / 2) + int((tmp[a[i]] - 1) * (tmp[a[i]] - 2) / 2))
    else:
        print(ans)