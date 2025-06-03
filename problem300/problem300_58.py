from fractions import gcd

A,B=map(int,input().split())
p=set([1])
g=gcd(A,B)
for d in range(2,g):
    while g%d==0:
        p.add(d)
        g//=d
    if (d*d>=g): break
if g>=2:
    p.add(g)
print(len(p))
