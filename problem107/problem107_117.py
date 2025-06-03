n = int(input())
x = input()
popcnt = x.count("1")

def powmod(lst,mod):
    if not mod: return
    d = 1
    for i in range(n)[::-1]:
        d %= mod
        lst[i] = d
        d *= 2

def xmod(mod):
    if not mod: return 
    res = 0
    d = 1
    for i in range(n)[::-1]:
        d %= mod
        if int(x[i]):
            res += d
            res %= mod
        d *= 2
    return res

def solve(x):
    res = 1
    while x != 0:
        popcnt = 0
        for i in range(20):
            if x>>i & 1: popcnt += 1
        x %= popcnt
        res += 1
    return res
    
powlst0 = [0]*n
powlst1 = [0]*n
powmod(powlst0,popcnt+1)
x0 = xmod(popcnt+1)
powmod(powlst1,popcnt-1)
x1 = xmod(popcnt-1)

for i in range(n):
    if int(x[i]):
        if popcnt == 1: print(0)
        else: print(solve((x1-powlst1[i])%(popcnt-1)))
    else: print(solve((x0+powlst0[i])%(popcnt+1)))