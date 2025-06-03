n = int(input())
x = list(map(int,input().split()))
x.sort()
ans = 9999999999999999
for p in range(x[0],x[n-1]+1):
    tmp = 0
    for j in range(n):
        tmp += (x[j] - p) ** 2
    ans = min(tmp,ans)
print(ans)
