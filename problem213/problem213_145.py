n = int(input())
x = list(map(int,input().split()))
a = min(x)
b = max(x) + 1
ans = 10 ** 8
for p in range(a,b):
    m = 0
    for i in range(n):
        m += (x[i] - p) ** 2
    ans = min(ans,m)
print(ans)