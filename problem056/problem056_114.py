n_m_str=input().split()
n_m=list(map(lambda i : int(i),n_m_str))
n,m=n_m[0],n_m[1]
a=[input() for i in range(n)]
A=[]
for i in a:
    A.append(i.split())
b=[input() for i in range(m)]
Ab=[]
for i in range(n):
    Ab.append(0)
for i in range(n):
    for j in range(m):
        Ab[i]+=int(A[i][j])*int(b[j])
for i in Ab:
    print(i)
