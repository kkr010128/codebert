a,b=map(int,input().split())
l=list(map(int,input().split()))
for i in range(b):
  a-=l[i]
print("Yes" if a<=0 else"No")