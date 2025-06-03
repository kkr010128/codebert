
a,b,c,d = map(int, input().split())


if a*b <= 0 and c*d <= 0:
    print(max([a*c, b*d]))
elif a*b <= 0 and c >= 0:
    print(b*d)
elif a*b <=0 and d <=0:
    print(a*c)
elif a>=0 and c*d<=0:
    print(b*d)
elif a>=0 and c>=0:
    print(b*d)
elif a>=0 and d<=0:
    print(a*d)
elif b<=0 and c*d<=0:
    print(a*c)
elif b<=0 and c>=0:
    print(b*c)
elif b<=0 and d<=0:
    print(a*c)