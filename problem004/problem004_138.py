def ok(a,b,c):
    return (a*a+b*b==c*c)

n=input()
for i in range(n):
    a,b,c=map(int,raw_input().split())
    if(ok(a,b,c) or ok(b,c,a) or ok(c,a,b)):
        print "YES"
    else:
        print "NO"