import fractions

A,B = (int(a) for a in input().split())
print(A * B // fractions.gcd(A,B))