k,n=map(int,input().split())
a=list(map(int,input().split()))
b=[]
for i in range(len(a)-1):
  b.append(a[i+1]-a[i])
  
b.append(abs(a[-1]-a[0]-k))

b.sort()
b[-1]=0
print(sum(b))