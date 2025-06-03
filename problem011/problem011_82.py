import math

def gcd(a,b):
    if a<b: a,b=b,a
    c=a%b
    if c==0:
        return b
    else:
        return gcd(b,c)
    
S=[ int(x) for x in input().split()]    
print(gcd(S[0],S[1]))
