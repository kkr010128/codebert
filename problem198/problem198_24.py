N=int(input())
A=["a","b","c","d","e","f","g","h","i","j"]
L=[{}for i in range(N+1)]
L[1]["a"]=1
#print(L)

for i in range(2,N+1):
    for j,k in L[i-1].items():
        for l in range(k+1):
            L[i][j+A[l]]=max(l+1,k)
#print(L[N])
ans=L[N].keys()
ans=list(ans)
ans.sort()
for i in range(len(ans)):
    print(ans[i])