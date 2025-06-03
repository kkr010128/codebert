A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)

if A == B == C :
    print('No')
elif A == B :
    print('Yes')
elif B == C :
    print('Yes')
elif C == A :
    print('Yes')
elif A == B == C :
    print('No')
else :
    print('No')