[N,K,S] = list(map(int,input().split()))
cnt = 0
output = []
if S != 10**9:
    for i in range(K):
        output.append(S)
    for i in range(N-K):
        output.append(S+1)
else:
    for i in range(K):
        output.append(S)
    for i in range(N-K):
        output.append(1)

print(*output)