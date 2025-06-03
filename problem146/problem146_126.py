import sys,math
input = sys.stdin.buffer.readline

mod = 1000000007
n = int(input())

ab = []
ang = dict()
rev = dict()
dg = 10**20
zero = 0

for i in range(n):
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        zero += 1
    elif a == 0:
        if 1 in ang:
            ang[1] += 1
        else:
            ang[1] = 1
    elif b == 0:
        if 1 in rev:
            rev[1] += 1
        else:
            rev[1] = 1
    elif a*b > 0:
        if a < 0 and b < 0:
            a,b = -a,-b
        g = math.gcd(a,b)
        a,b = a//g,b//g

        if a*dg + b in ang:
            ang[a*dg + b] += 1
        else:
            ang[a*dg + b] = 1
    else:
        a,b = abs(a),abs(b)
        g = math.gcd(a,b)
        a,b = a//g,b//g

        if b*dg + a in rev:
            rev[b*dg + a] += 1
        else:
            rev[b*dg + a] = 1

rest = n - zero

res = 1

for e in ang:
    if e in rev:
        res = res*(pow(2,ang[e],mod) + pow(2,rev[e],mod) - 1)%mod
        rest -= ang[e] + rev[e]

res = res*pow(2,rest,mod)%mod - 1 + zero

print(res%mod)
