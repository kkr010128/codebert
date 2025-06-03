mod = 10**9+7
N, K = map(int,input().split())
A = sorted(list(map(int,input().split())))

pi = 1
ni = 0
ans = 1
i = 0
while i < K-1:
  if A[ni]*A[ni+1] > A[-pi]*A[-pi-1]:
    ans = ans*A[ni]*A[ni+1]%mod
    ni += 2
    i += 2
    
  else:
    ans = ans*A[-pi]%mod
    pi += 1
    i += 1
    
if i == K-1:
  ans = ans*A[-pi]%mod
  
if A[-1]<0 and K%2==1:
  ans = 1
  for i in A[N-K:]:
    ans = ans*i%mod

print(ans)
