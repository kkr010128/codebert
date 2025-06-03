def gcd(a,b):
  if b ==0:
    return a
  else:
    return gcd(b, a%b)
  
  
A,B = map(int, input().split())
A,B = (A,B) if A>B else (B,A)

print(int(A/gcd(A,B)*B))