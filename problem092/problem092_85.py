X, K, D = map(int, input().split())

N = abs(X) // D
O = abs(X) - N * D

if O <= (D - O):
    pass
else:
    N += 1
    O = D - O
    
if N >= K:
    print(abs(X) - K * D)
else:
    if (K - N) % 2 == 0:
        print (O)
    else:
        print(D - O)