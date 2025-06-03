N,K=map(int,input().split())
if N%K != 0:
    if abs(K-N%K)<N:
        print(K-N%K)
    else:
        print(N)
else:
    print(0)
