x=[]
z=[]
A,b=map(int,input().split())
for i in range(0,A):
 a=list(map(int,input().split()))
 x.append(a)
for s in range(0,b):
    q=int(input())
    z.append(q)
    
for i in range(A):
  l=0
  for s in range(b):
    l += x[i][s]*z[s]
  print(l)