import math, sys

X = int(input())

if int(X**(1/5)) **5 ==X:
    print(*[ int(X**(1/5)) , 0])
    sys.exit()

for i in range(1,10**7):
    A = i**5
    B = A - X
    C = X - A

    if B > 0 and int(B**(1/5)) **5 == B:
        print(*[ i , int(B**(1/5)) ])
        sys.exit()

    if C > 0 and int(C**(1/5)) **5 ==C:
        print(*[ i , - int(C**(1/5)) ])
        sys.exit()