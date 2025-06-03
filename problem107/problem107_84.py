from collections import defaultdict
n,x = open(0).read().split()
n = int(n)
cnt = x.count('1') 
digits = list(map(int, list(x)))
x = int(x, 2)

d = defaultdict(int)
d[0] = 0
def calc(m):
    if m not in d:
        nxt = m % bin(m).count('1')
        d[m] = calc(nxt) + 1
    return d[m]

mmod = cnt - 1
pmod = cnt + 1

if mmod:
    mx = x % mmod
px = x % pmod

mbase = 1
pbase = 1

ans = []
while digits:
    digit = digits.pop()
    
    if digit and not mmod:
        ans.append(0)
    else:
        if digit:
            nx = (mx - mbase)%mmod
        else:
            nx = (px + pbase)%pmod
        ans.append(calc(nx) + 1)

    if mmod > 0:
        mbase = (mbase * 2) % mmod
    pbase = (pbase * 2) % pmod

while ans:
    print(ans.pop())