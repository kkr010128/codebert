n,k=map(int,input().split())
a=n//k
print(min(abs(n-a*k),abs(n-(a+1)*k)))