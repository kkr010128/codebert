A, B, K = map(int, input().split())
if A >= K: 
    A -= K
else:
    B = max((A + B) - K, 0)
    A = 0
print(A,  B)