def gcd(a,b):
    if(b):
        return gcd(b,a%b)
    return a

l = raw_input().split()
if(int(l[0]) > int(l[1])):
    print gcd(int(l[0]),int(l[1]))
else:
    print gcd(int(l[1]),int(l[0]))
