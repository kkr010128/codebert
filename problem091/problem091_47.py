N=int(input())
L=list(map(int,input().split()))
count=0
for a in range(N):
    for b in range(N):
        for c in range(N):
            if L[a]<(L[b]+L[c]) and L[b]<(L[a]+L[c]) and L[c]<(L[b]+L[a]) and L[a]!=L[b] and L[a]!=L[c] and L[c]!=L[b] and a<b<c:
                count=count+1
            else:
                continue
print(count)