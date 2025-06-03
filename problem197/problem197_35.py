a,b,c = map(int, input().split())
s =c-a-b
t = s**2 - 4*a*b
if s >=0 and t > 0:
    print('Yes')
else:
    print('No')