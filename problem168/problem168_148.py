n,m=map(int,input().split())
a =list(map(int,input().split()))
day = 0
for i in range(m):
    day += a[i]
print(-1 if day>n else n - day)