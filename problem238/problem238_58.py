N,K,S = map(int,input().split())
ans = []
for i in range(K):
    ans.append(S)
for j in range(N-K):
    if not S == 1000000000:
        ans.append(S+1)
    else:
        ans.append(S-1)
for l in ans:
    print(l,end=" ")
print()      