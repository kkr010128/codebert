import math

a,b = map(int,input().split())

c = math.ceil
min8, max8 = c(a*12.5), c((a+1)*12.5)
min10, max10 = c(b*10), c((b+1)*10)

l8, l10 = list(range(min8, max8)), list(range(min10, max10))
s8, s10 = set(l8), set(l10)

ss = s8 & s10
#print(min8, max8, min10, max10)
print(min(ss) if len(ss) >0 else -1)
#print(238*0.08)