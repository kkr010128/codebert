A, B, K = list(map(int, input().split()))

if A <= K:
    K = K - A
    A = 0
    if B <= K:
        K = K - B
        B = 0
    else:
        B = B - K
else:
    A = A - K 
        
print(str(A) + ' ' + str(B))