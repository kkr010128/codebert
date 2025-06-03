S = list(str(input()))
S.reverse()
mod = 2019
rem = [0]*mod
num = 0
rem[num] += 1
d = 1
ans = 0
for s in S:
  num += int(s) * d
  num %= mod
  d *= 10
  d %= mod
  rem[num] += 1
for r in rem:
  ans += r*(r-1)//2
print(ans)