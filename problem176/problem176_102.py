def powmod(x, n,mod):
  if n == 0:
   return 1
  K = 1
  while n > 1:
   if n % 2 != 0:
    K = K * x%mod
    x = x ** 2%mod
    n = (n - 1) // 2
   else:
    x = x ** 2%mod
    n = n // 2%mod
  return K * x # 指数を割り続け n が 1 に至ったら終了
N,K = map(int,input().split())
mod=10**9+7
ans=[0]*(K+1)
for i in range(K):
 b=int(K/(K-i))
 if b==1:
  ans[K-i]+=1
 else:
  ans[K-i]+=powmod(b, N,mod)
  ans[K-i]%=mod
  for j in range(b-1):
   ans[K-i]-= ans[(K-i)*(j+2)]
   ans[K-i]%=mod
c=0
for i in range(K+1):
 c+=ans[i]*i
 c%=mod
print(c)
