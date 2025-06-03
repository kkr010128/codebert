a,b,n=map(int,input().split())
if a%n == 0 and b%n == 0:
    print((b//n) - (a//n) + 1)
else:
    print((b//n) - (a//n))