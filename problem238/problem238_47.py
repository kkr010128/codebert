N,K,S=[int(x) for x in input().rstrip().split()]
ans=[]
if S==10**9:
    for i in range(N):
        if i+1<=K:
            ans.append(S)
        else:
            ans.append(1)
else:
    for i in range(N):
        if i+1<=K:
            ans.append(S)
        else:
            ans.append(S+1)
print(*ans)

