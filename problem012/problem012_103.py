import math

p = [2]
    
def isprime(x):
    if x == 2:
        return True
    if x == 3:
        return True
    if max(p) < x**0.5:
        for j in range(max(p), math.floor(x**0.5) + 1):
            if all([j % k != 0 for k in p]):
                p.append(j)
    i = 0
    while i <= len(p)-1:
        if x%p[i] == 0:
            return False
        if p[i] > x**0.5:
            break;
        i += 1
    return True


n = int(input())
res = 0
for i in range(n):
    k = int(input())
    if isprime(k):
        res += 1
print(res)