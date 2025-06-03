A,B = list(map(int,input().split()))
# A=10**10
# B=10**12

def gcd(a,b):
    x=min(a,b)
    y=max(a,b)
    
    while y%x != 0:
#         print(x,y)
        x_= y%x
        y = x
        x = x_
    return x

gcd = gcd(A,B)

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

P_F=[1]
P_F.extend(prime_factorize(gcd))
print(len(set(P_F)))