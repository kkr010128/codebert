a, b, c, d = input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
def m():
        if a>=0 and d<=0:
            max=a*d
            print(max)
        elif a>=0 and c>=0:
            max=b*d
            print(max)
        elif b<=0 and c>=0:
            max=b*c
            print(max)
        elif b<=0 and d<=0:
            max=a*c
            print(max)
        elif a<=0 and b>=0 and c<=0 and d>=0:
            if a*c>=b*d:
                max=a*c
                print(max)
            else:
                max=b*d
                print(max)
        elif a>=0 and c<=0 and d>=0:
            max=b*d
            print(max)
        elif b<=0 and c<=0 and d>=0:
            max=a*c
            print(max)
        elif a<=0 and b>=0 and c>=0:
            max=b*d
            print(max)
        elif a<=0 and b>=0 and d<=0:
            max=a*c
            print(max)

m()