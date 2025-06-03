h,n= map(int, input().split())
a = list(map(int,input().split()))
for i in range(n):
    h -= a[i]
print("Yes" if h <=0 else "No")