n = int(input())
A = list(map(int,input().split()))

L = [0]*(n+2)
R = [0]*(n+2)
L[n] = A[n]
R[n] = A[n]

for i in range(n,-1,-1):
  L[i] = A[i] + (L[i+1]+1)//2
  R[i] = A[i] + R[i+1]
  
if L[0]>1:
  print(-1)
else:
  tmp = 1
  ans = 0
  for i in range(n+1):
    ans += tmp
    tmp -= A[i]
    tmp = min(tmp*2,R[i+1])    
  print(ans)    