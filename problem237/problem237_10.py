n=int(input())
R=[]
for _ in range(n):
  x,l=map(int,input().split())
  R.append([x-l,x+l])

R=sorted(R,key=lambda x:x[1])
ans=n
for i in range(1,n):
  if R[i][0]<R[i-1][1]:
    ans-=1
    R[i][1]=R[i-1][1]
  
print(ans)