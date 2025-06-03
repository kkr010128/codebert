X,N = map(int,input().split())
P = list(map(int,input().split()))

a = list(range(102))
for i in range(N):
    a[P[i]] = -2
m = 102
for i in range(102):
    if m > (abs(X - a[i])):
        m = (abs(X - a[i]))
        ans = a[i]
print(ans)