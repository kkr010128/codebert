N, K = map(int,input().split())
n_mod = N % K
print(min(n_mod, K-n_mod))