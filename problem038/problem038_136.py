a,b=input().split()
c=int(a);d=int(b)

if c>=-1000 and d<=1000:
    if c>d:
        print("a > b")

    elif c<d:
        print("a < b")

    else:
        print("a == b")