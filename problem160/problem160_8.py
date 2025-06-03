import itertools
n,m,q=list(map(int,input().split()))
abcd=[[] for i in range(q)]
for i in range(q):
    abcd[i]=list(map(int,input().split()))
ans=0
l=list(itertools.combinations_with_replacement([a for a in range(1,m+1)],n))
x=(len(l))
for i in range(x):
    e=l[i]
    
    wa=0
    for t in range(q):
        if e[abcd[t][1]-1]-e[abcd[t][0]-1]==abcd[t][2]:
            wa+=abcd[t][3]
    ans=max(ans,wa)
print(ans)
            

