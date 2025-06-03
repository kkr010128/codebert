N = int(input())

def divisor(n):
  res = []
  for i in range(1, int(n**0.5)+1):
    if n%i!=0: continue
    res.append(i)
    if i*i != n: res.append(n//i)
  return res

ans = 0

d = []
for x in divisor(N):
  if x==1: continue
  tmp = N
  while tmp%x==0: tmp //= x
  tmp %= x
  if tmp == 1: ans += 1

ans += len(divisor(N-1)) - 1
print(ans)