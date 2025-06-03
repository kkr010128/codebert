a,b,k=map(int,input().split())
t=min(a,k)
s=min(b,k-t)
print(a-t,b-s)