a,b=map(int,input().split())
def p(n):
    a = set([1])
    while n % 2 == 0:
        a.add(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.add(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.add(n)
    return a
s=p(a)
l=list(s)
for x in l:
  if b%x!=0:
    s.remove(x)
print(len(s))