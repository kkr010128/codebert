k = int(input())

sum = 0

def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a % b)


for a in range(1, k + 1):
    for b in range(1, k + 1):
        ab_gcd = gcd(a, b)
        for c in range(1, k + 1):
            abc_gcd = gcd(c, ab_gcd)
            sum += abc_gcd
        
print(sum)
