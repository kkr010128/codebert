def warshal(data):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                data[i][j]=min(data[i][j],data[i][k]+data[k][j])
    return data
n,m,l=map(int,input().split())
inf=float("inf")
data=[[inf]*n for i in range(n)]
for i in range(m):
    a,b,c=map(int,input().split())
    data[a-1][b-1]=c
    data[b-1][a-1]=c
for i in range(n):
    data[i][i]=0
data=warshal(data)
for i in range(n):
    for j in range(n):
        if data[i][j]<=l:
            data[i][j]=1
        else:
            data[i][j]=inf
for i in range(n):
    data[i][i]=0
data=warshal(data)
q=int(input())
st=[]
for i in range(q):
    s,t=map(int,input().split())
    st.append([s-1,t-1])
for s,t in st:
    if data[s][t]==inf:
        print(-1)
    else:
        print(data[s][t]-1)