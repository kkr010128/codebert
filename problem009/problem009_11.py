def breathSerch(P,N):
    n=len(P)-1
    m=1
    QQ=[N[1]]
    while(QQ != []):
        R=[]
        for Q in QQ:
            for i in range(1,n+1):
                if Q[i]==1 and P[i]==-1:
                    P[i]=m
                    R.append(N[i])
        QQ = R
        m=m+1
    
n = int(input())
A = [[0 for j in range(n+1)] for i in range(n+1)]


for i in range(n):
    vec = input().split()
    u = int(vec[0])
    k = int(vec[1])
    nodes = vec[2:]
    for i in range(int(k)):
        v = int(nodes[i])
        A[u][v] = 1

P=[-1 for i in range(n+1)]
P[1]=0
breathSerch(P,A)
for i in range(1,n+1):
    print(i,P[i])