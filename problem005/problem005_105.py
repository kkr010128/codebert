from sys import stdin
import math

def GCD(a,b):
    if(a%b==0):
        return b
    else:
        c = a%b
        return GCD(b,c)

def LCM(a,b):
    gcd = GCD(a,b)
    return int(a*b/gcd)

for line in stdin:
    a,b = line.split(" ")
    a = int(a)
    b = int(b)
    gcd = GCD(a,b)
    lcm = LCM(a,b)

    print(str(gcd)+" "+str(lcm))


