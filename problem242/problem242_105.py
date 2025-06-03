# x^n % mod
def pow_k(x, n, mod):
  if n == 0:
    return 1

  K = 1
  while n > 1:
    if n % 2 != 0:
      K = (x * K) % mod
        
    x = (x * x) % mod

    n //= 2

  return (x * K) % mod

def main():
  MOD = 10 ** 9 + 7
  n,k = map(int,input().split())
  a = sorted(list(map(int,input().split())))
  
  g_k = 1
  for i in range(1,k):
    g_k *= i
    g_k %= MOD
    
  gyakugen = pow_k(g_k,MOD-2,MOD)
  array = [0] * (n+1)
  array[k-1] = g_k
  
  for i in range(k, n+1):
    array[i] = array[i-1] * i * pow_k(i-k+1,MOD-2,MOD)
    array[i] %= MOD
    
  ans = 0
  for i in range(n):
    if i-k+1 >= 0:        
      ans += array[i] * gyakugen * a[i]
      
    if n-i-k >= 0:
      ans -= array[n-i-1] * gyakugen * a[i]
      
    ans %= MOD
      
  print(ans)

main()