A, B, K = map(int,input().split())

A1 = max(A-K,0)
K1 = max(K-A,0)

if K1 == 0:
    B1 = B
else:
    B1 = max(B-K1,0)

print(A1,B1)