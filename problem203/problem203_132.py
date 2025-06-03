import math

a,b = [int(x) for x in input().split()]

ma = int(a//0.08)
mb = int(b//0.1)


fmindi = False
mindi = 9999999999999

for x in range(min(ma,mb),max(ma,mb)+2):
    j = math.floor(x*0.08)
    e = math.floor(x*0.1)
    if j == a and e == b:
        fmindi = True
        mindi = min(mindi,x)

print(mindi if fmindi else -1)
