n = int(input())

MOD = 1000000007

def mod(n):         
  return n % MOD

def modpow(a, n):   #mod(a**n)を高速で求める
    res = 1  
    digit = len(str(bin(n))) - 2
    for i in range(digit):
      if (n >> i) & 1:
        res *= mod(a)
        res = mod(res)
      a = mod(a**2)
    return mod(res)
  
ans = modpow(10, n)
ans -= 2*modpow(9, n)
ans += modpow(8, n)
print(mod(ans))