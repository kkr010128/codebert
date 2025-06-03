a,b,c = map(int, input().split())
A = min(min(a, b),c)
C = max(max(a,b),c)
B = (a+b+c) - (A+C)
print(A, B, C)

