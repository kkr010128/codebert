from collections import Counter
s=input()
n=len(s)
MOD=2019
L=[0]
for i in range(n):
    l=(int(s[n-1-i])*pow(10,i,MOD)+L[i])%MOD
    L.append(l)
LC=Counter(L)
r=0
for v in LC.values():
    r+=v*(v-1)//2
print(r)