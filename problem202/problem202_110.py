N,A,B = map(int,input().split())

p = N // (A+B)
q = N % (A+B)
if q > A:
    r = A
else:
    r = q
print(A * p + r)