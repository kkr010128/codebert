import fractions 
a,b=map(int,input().split())
c = fractions.gcd(a,b)
print(int((a*b)/c))