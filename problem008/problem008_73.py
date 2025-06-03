T = [0]

def curserch(N,k,T,P,n):
    T[0] = T[0]+1
    P[k]["d"] = T[0]
    for i in range(1,n+1):
        if N[k][i]==1 and P[i]["d"]==0:
            curserch(N,i,T,P,n)
            T[0] = T[0]+1
            P[i]["f"]=T[0]


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

P=[{"d":0} for i in range(n+1)]
for i in range(1,n+1):
    if P[i]["d"]==0:
        curserch(A,i,T,P,n)
        T[0] = T[0]+1
        P[i]["f"]=T[0]
for i in range(1,n+1):
    print(i,P[i]["d"],P[i]["f"])