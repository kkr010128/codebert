S = input()
N = len(S)
mod = 2019

cnt = [0 for _ in range(2019)]
S = S[::-1]
wk = 0
cnt[0] = 1

for i in range(0,N):
  wk = (wk + int(S[i]) * pow(10,i,mod)) % mod
  #print(i,wk)
  cnt[wk] += 1
  
ans = 0
for i in range(2019):
  m = cnt[i]
  ans += m * (m-1) // 2
  
print(ans)