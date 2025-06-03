n = int(input())
mod = 10 ** 9 + 7
start,zero,nine,ans = 1,0,0,0
for i in range(n):
  ans = (ans * 10 + zero + nine) % mod
  zero = (zero * 9 + start) % mod
  nine = (nine * 9 + start) % mod
  start = (start * 8) % mod
print(ans)