N,K = (int(x) for x in input().split())
p = N % K
if p < (K-p):
    print(p)
else:
    print(K-p)
