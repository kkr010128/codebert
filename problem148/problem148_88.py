A,B,C,K = [int(x) for x in input().split()]

if(A >= K):
    print(K)
    exit()
K = K - A
if(B >= K):
    print(A)
    exit()
K = K - B
print(A-K)
