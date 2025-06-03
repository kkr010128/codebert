def isPrime(n):
    if n==2 or n==3:
        return True
    elif n%2==0:
        return False
    else:
        i = 2
        while i**2 <= n:
            if n%i == 0:
                return False
            i += 1
    return True
    
r = []
n = int(input())
for i in range(n):
    p = int(input())
    if isPrime(p):
        if p not in r:
            r.append(p)

print(len(r))