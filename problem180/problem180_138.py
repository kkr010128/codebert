n,k=map(int,input().split())
s=n%k
t=k-s
print(min(s,t))