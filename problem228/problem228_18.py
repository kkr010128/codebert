def ans(n,k):
  if n==0:
    return k
  else:
    return ans(n//2,k)*2+1
N=int(input())
print(ans(N,0))