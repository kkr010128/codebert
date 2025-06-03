A,B,C=map(int,input().split())
result=0
if A == B:
    if A != C and B != C:
        result+=1
elif A == C:
    if A != B and B != C:
        result+=1
elif B == A:
    if B != A and C != B:
        result+=1
elif B ==C:
    if B != A and A != C:
        result+=1
elif C == A:
    if C != B and A == B:
        result+=1
elif C == B:
    if C != A and A == B:
        result+=1
if result==1:
    print('Yes')
else:
    print('No')