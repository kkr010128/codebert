import sys

def gcd(a,b):
    if(b):
        return gcd(b,(a%b))
    else:
        return a

def lcm(a,b):
    return a*b/gcd(a,b)

a = ""
for input in sys.stdin:
    a += input
l = a.split()
for i in range(0,len(l),2):
    if(int(l[i]) > int(l[i+1])):
        print gcd(int(l[i]),int(l[i+1])),lcm(int(l[i]),int(l[i+1]))
    else:
        print gcd(int(l[i+1]),int(l[i])),lcm(int(l[i+1]),int(l[i]))
