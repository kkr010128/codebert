from collections import Counter
s=input()
n=len(s)
M=[0]
mod=2019
for i in range(n):
	m=(M[-1]+int(s[n-1-i])%mod*pow(10,i,mod))%mod
	M.append(m)
MC=Counter(M)
r=0
for v in MC.values():
	if v>1:
		r+=v*(v-1)//2
print(r)