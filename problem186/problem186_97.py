k,n=map(int,input().split())
h=list(map(int,input().split()))
l=[]
for i in range(n-1):
  l.append(h[i+1]-h[i])
l.append(h[0]+k-h[n-1])
ll=sorted(l,key=int,reverse=True)
print(k-ll[0])
