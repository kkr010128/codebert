n,K = list(map(int,input().split()))
mod = 10**9+7
ans = 0
for k in range(K,n+2):
  #ans += (n+1)*n//2 -(n+1-k)*(n-k)//2-k*(k-1)//2 + 1
  #ans += (n**2+n)//2 - (n**2-n*k+n-k-n*k+k**2)//2 - (k**2-k)//2 + 1
  #ans += (n**2+n - (n**2-n*k+n-k-n*k+k**2) -k**2 + k)//2 + 1
  #ans += (n**2 + n - n**2 + n*k - n + k + n*k - k**2 - k**2 + k)//2 + 1
  #ans += (2*n*k + 2*k - 2*k**2)//2 + 1
  ans += n*k - k**2 + k  + 1
print(ans%mod)