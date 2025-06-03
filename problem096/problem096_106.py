N,D = map(int,input().split())
A=[[int(i) for i in input().split()] for _ in range(N)]
ans=int()

for i in range(N):
  if A[i][0]*A[i][0]+A[i][1]*A[i][1]<=D*D:
    ans+=1
print(ans)
  
