S = list(input())
NS = [s for s in S]
K = int(input())
L = len(S)

if "".join(S) == S[0] * L:
  print(L * K // 2)
  exit()

ans = 0
for i in range(L-1):
  f_s = S[i]
  s_s = S[i+1]
  if f_s == s_s:
    S[i+1] = '-'
    ans += 1

# 先頭と末尾が異なる
if S[0] != S[-1]:
  ans *= K
# 一緒
else:
  a = 0
  for i in range(L):
    if NS[i] == NS[0]:
      a += 1
    else:
      break
  
  b = 0
  for i in range(L)[::-1]:
    if NS[i] == NS[-1]:
      b += 1
    else:
      break
      

  ans *= K
  #t = (- (-a // 2)) + (- (-b // 2)) - (- (-a-b) // 2)
  #t = -(-a // 2) - (-b // 2) + (-(a+b) // 2)
  t = a // 2 + b // 2 - (a+b) // 2
  ans -= t * (K-1)
  
print(ans)
  
