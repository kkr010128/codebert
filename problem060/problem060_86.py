n,m,l=list(map(int,input().split()))

m_A=[list(map(int,input().split())) for i in range(n)]

m_B=[list(map(int,input().split())) for i in range(m)]

for i in range(n):
    t=[]
    for k in range(l):
        s=0
        
        for j in range(m):
            s+=m_A[i][j]*m_B[j][k]
        t.append(s)
    print(*t)