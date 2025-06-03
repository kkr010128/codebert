a,b=map(int,input().split())
l=list(map(int,input().split()))
z=0
l=sorted(l)
for i in range(a-b):
  z+=l[i]
print(z)