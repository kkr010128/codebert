A,B,K = list(map(int, input().split()))
if A > K:
    A -= K
else:
    K -= A
    A = 0
    
    if B > K:
        B -= K
    else:
        B = 0
print(A,B)

A -= min(A, K)



