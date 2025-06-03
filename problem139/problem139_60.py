a,b,c,d,e = map(int,input().split())
x = abs(a - c) * 60 - b + d - e
if x < 0:
    print(0)
else:
    print(x)