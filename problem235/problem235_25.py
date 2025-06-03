import fractions

N = int(input())
A = list(map(int,input().split()))
MOD = 10** 9 + 7
lcm = 1
for a in A:
    lcm = a // fractions.gcd(a,lcm) * lcm

print(sum(lcm//a for a in A)%MOD)