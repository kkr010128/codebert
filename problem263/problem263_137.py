n = int(input())
a = list(map(int,input().split()))
MOD = 10 ** 9 + 7
digit = 60
o=[0]*digit
z=[0]*digit

for i in a:
  for j in range(digit):
    if (i >> j) & 1:
      o[j] += 1
    else:
      z[j] += 1
ans = 0    
for j in range(digit):
  ans += (o[j]*z[j]*pow(2,j,MOD))
print(ans % MOD)