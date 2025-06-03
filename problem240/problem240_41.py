n,m = map(int,input().split())

dac = {}
for i in range(1,n+1):
    dac[str(i)] = 0
dwa = {}
for i in range(1,n+1):
    dwa[str(i)] = 0

for i in range(m):
    p,s = input().split()
    if s == 'AC':
        dac[p] = 1
    if s == 'WA' and dac[p] == 0:
        dwa[p] += 1

ac = 0
wa = 0

for k,v in dac.items():
    ac += v

for k,v in dwa.items():
    if dac[k] == 1:
        wa += v

print(ac,wa)