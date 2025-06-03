S = input()
Sliststr = list(S)
Slist = [int(s) for s in Sliststr]
Smod = [0]
mod10 = [1]
count = [0]*2019
ans = 0
for i in range(len(S)-1):
  mod10.append(mod10[i]*10%2019)
for i in range(len(S)):
  Smod.append((Smod[i]+Slist[-i-1]*mod10[i])%2019)
for i in range(len(Smod)):
  count[Smod[i]] += 1
for i in range(2019):
  ans += count[i] * (count[i]-1) // 2
print(ans)