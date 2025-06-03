A, B, C, K = map(int ,input().split())

Xa = min(K,A)
K2 = K - Xa
Xb = min(K2,B)
Xc = K2 - Xb

print(Xa - Xc)