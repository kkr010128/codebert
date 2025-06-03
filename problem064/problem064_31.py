S=str(input())
P=str(input())

A=S.count(P)

if A==0:
    B=S+S
    C=B.count(P)
    if C==0:
        Q=0
    else:
        Q=C
else:
    Q=A
    


if Q==0:
    print('No')
    
else:
    print('Yes')
