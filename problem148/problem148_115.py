A, B, C, K = [int(v) for v in input().split()]

s = 0
while K:
    if A and K:
        if K >= A:
            K -= A
            s += A
            A -= A
        else:
            s += K
            K -= K
    if B and K:
        if K >= B:
            K -= B
        else:
            K -= K
    
    if C and K:
        if K >= C:
            K -= C
            s -= C
            C -= C
        else:
            s -= K
            K -= K

        
print(s)