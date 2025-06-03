n,k=map(int,input().split())
ar=list(map(int,input().split()))
ar.sort()
pos=0
for i in range(k):
  pos+=ar[i]
print(pos)