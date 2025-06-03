n = int(input())
ls = list(map(int,input().split()))
mon = 1000
beet = 0
p = []
m = []
if ls[1]-ls[0] > 0:
    beet += int(mon//ls[0])
    mon -= ls[0]*int(mon//ls[0])
    be = True
else:
    be = False
for i in range(n-1):
    if ls[i] < ls[i+1]:
        if be == False:
            beet += int(mon//ls[i])
            mon -= ls[i]*int(mon//ls[i])
            be = True
    if ls[i] > ls[i+1]:
        if be == True:
            mon += ls[i] * beet
            beet = 0
            be = False
if beet > 0:
    mon += beet*ls[-1]
print(mon)