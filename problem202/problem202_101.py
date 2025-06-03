N,A,B = map(int,input().split())

if N % (A+B) > A:
  C = A
elif N % (A+B) <= A:
  C = N % (A+B)
  
print((N//(A+B))*A + C)
