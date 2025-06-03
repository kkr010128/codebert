N,K,S = map(int,input().split())
if S != 10**9:
    for _ in range(K):
        print(S,end = ' ')
    for _ in range(N - K):
        print(10**9,end = ' ')
else:
    for _ in range(K):
        print(10**9,end = ' ')
    for _ in range(N - K):
        print(1,end = ' ')
print()
