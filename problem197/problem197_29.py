a,b,c = map(int,input().split())
an = c-a-b
ab = a*b
if an <= 0:
    print("No")
else:
    an = an*an
    if an-4*ab > 0:
        print("Yes")
    else:
        print("No")