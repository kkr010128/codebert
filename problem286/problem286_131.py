a,b = (int(x) for x in input().split())

if 0 < a < 10 and  0 < b < 10:
    print(a*b)
else:
    print(-1)