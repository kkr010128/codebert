def gcd(s,t):
    if t==0:
        return s
    else:
        return gcd(t, s%t)

s, t = [int(x) for x in input().split()]

GCD = gcd(s,t)
LCM = (s*t)//GCD
print(LCM)