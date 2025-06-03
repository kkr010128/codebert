X,Y = map(int,input().split())
M = max(X,Y)
m = min(X,Y)
mod = 10 ** 9 + 7

con = (X + Y) // 3
dif = M - m
n = (con - dif) // 2

if (X + Y) % 3 != 0 or n < 0:
  print(0)
  
else:
  def comb(n, r):
    n += 1
    over = 1
    under = 1
    for i in range(1,r + 1):
      over = over * (n - i) % mod
      under = under * i % mod
    #powでunder ** (mod - 2) % modを実現、逆元を求めている
    return over * pow(under,mod - 2,mod) % mod
  
  ans = comb(con,n)
  
  print(ans)