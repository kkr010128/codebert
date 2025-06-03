t = int(input())
mod = 10**9 + 7

if t==1:
  print(0)
else:
  kans = 1
  for i in range(t):
    kans *= 10
    kans = kans % mod
  
  ans = 1
  for i in range(t):
    ans *= 9
    ans = ans % mod
    
  bans = 1
  for i in range(t):
    bans *= 8
    bans = bans % mod
    
  f = kans - ans*2 + bans
  f = f%mod
  
  print(f)
