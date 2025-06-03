a,b=input().split()
A=a*int(b)
B=b*int(a)
if A[0] > B[0]:
    print(B)
else:
    print(A)