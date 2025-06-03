a,b,c = map(int, input().split())

d = c - a - b
e = 4*a*b

if(d>0 and d**2 > e):
    print('Yes')
else:
    print('No')