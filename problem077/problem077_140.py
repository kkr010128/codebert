

a,b,c,d=map(int, input().split())
if b<0 and c>0:
    print(c*b)
elif d<0 and a>0:
    print(d*a)
elif b>=0 or d>=0:
    print(max(b*d,a*c))
else:
    print(a*c)
