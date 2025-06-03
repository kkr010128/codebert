import sys

def gcd(inta, intb):
    large = max(inta, intb)
    small = min(inta,intb)
    mod = large % small
    if mod ==0:
        return small
    else:
        return gcd(small, mod) 
    
def lcm(inta, intb, intgcd):
    return (inta * intb // intgcd)

sets = sys.stdin.readlines()
for line in sets:
    a, b = map(int, line.split())
    c = gcd(a, b)
    print(c, lcm(a, b, c))