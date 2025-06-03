a,b,n = map(int,input().split())
if b <= n:
    k = b-1
else:
    k = n
m = int(k*a/b) - a*int(k/b)
print(m)