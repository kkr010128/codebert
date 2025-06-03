N = int(input())
A = list(map(int,input().split()))
M = max(A)
X = [1]*(M+1)
for a in A:
  X[a]-=1
  for i in range(a*2,M+1,a):
    X[i]=-2 

ans = 0
for a in A:
  if X[a]>=0:
    ans+=1
print(ans)

