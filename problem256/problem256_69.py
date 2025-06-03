a,b=map(int,input().split())
import fractions
r=(a*b)//fractions.gcd(a,b)
print(r)