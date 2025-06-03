def gcd(a, b): 
    while b: 
        a, b = b, a % b 
    return a 
def lcm(a, b): 
    return a * b // gcd (a, b) 

c,d=[int(i) for i in input().split()]

print(gcd(c,d))