N=int(input())
S=input()

res=0
R=[]
G=[]
B=[]
r,g,b=0,0,0
for i in range(N):
    if S[i]=='R':
        r+=1
    elif S[i]=='G':
        g+=1
    else:
        b+=1
    R.append(r)
    G.append(g)
    B.append(b)
    
for i in range(N):
    for j in range(N):
        if not i<j:
            continue
        k=S[2*j-i] if 2*j-i<N else 'A'
        if set([S[i],S[j]])==set(['R','G']):
            res+=B[-1]-B[j]-(k=='B')
        elif set([S[i],S[j]])==set(['B','G']):
            res+=R[-1]-R[j]-(k=='R')
        elif set([S[i],S[j]])==set(['R','B']):
            res+=G[-1]-G[j]-(k=='G')
print(res)