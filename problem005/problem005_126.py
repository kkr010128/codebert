import fractions
while 1:
    try:
        a,b=map(int,input().split())
        c=fractions.gcd(a,b)
        print(c,(a*b)//c)
    except:break