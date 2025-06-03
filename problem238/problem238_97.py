N,K,S = map(int,input().split())
A = [S for i in range(K)]
if S<10**9:
    A += [S+1 for i in range(N-K)]
else:
    A += [1 for i in range(N-K)]
print(*A)