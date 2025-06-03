import sys
input = sys.stdin.readline

N = int(input())
op = []
ed = []
mid = [0]
dg = 10**7

for _ in range(N):
    s = list(input())
    n = len(s)-1

    a,b,st = 0,0,0
    for e in s:
        if e == '(':
            st += 1
        elif e == ')':
            if st > 0:
                st -= 1
            else:
                a += 1
    st = 0
    for i in range(n-1,-1,-1):
        if s[i] == ')':
            st += 1
        else:
            if st > 0:
                st -= 1
            else:
                b += 1
    if a > b:
        ed.append(b*dg + a)
    elif a == b:
        mid.append(a)
    else:
        op.append(a*dg + b)

op.sort()
ed.sort()

p = 0
for e in op:
    a,b = divmod(e,dg)
    if p < a:
        print('No')
        exit()
    p += b-a

q = 0
for e in ed:
    b,a = divmod(e,dg)
    if q < b:
        print('No')
        exit()
    q += a-b

if p == q and p >= max(mid):
    print('Yes')
else:
    print('No')
