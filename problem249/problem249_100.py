a,b,k = map(int,input().split())
t1 = min(a,k)
k -= t1
a -= t1
t2 = min(b,k)
k -= t2
b -= t2
print(a,b)