n = int(input())
MOD = 1000000007
 
s = [0]*2020
s[0]=1
s[1]=0
s[2]=0
for i in range(3,n+1,1):
  s[i] = (s[i] + sum(s[:(i-2)])) % MOD
print(s[n])