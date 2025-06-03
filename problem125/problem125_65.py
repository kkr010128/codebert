def gcd(a,b):
    # assume a,b are +ve integers.
    if a>b:
        a,b = b,a
    if b%a==0:
        return a
    
    return gcd(a,b%a)
print(360//(gcd(360,int(input()))))