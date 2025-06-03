N,K=map(int,input().split())
R,S,P=map(int,input().split())
T=input()

ans=0
A=[]
for i in range(K):
    if T[i]=='r':
        ans+=P
        A.append('p')
    elif T[i]=='s':
        ans+=R
        A.append('r')
    else:
        ans+=S
        A.append('s')

for i in range(K,N):
    if T[i]=='r':
        if A[i-K]!='p':
            ans+=P
            A.append('p')
        else:
            A.append('x')
    elif T[i]=='s':
        if A[i-K]!='r':
            ans+=R
            A.append('r')
        else:
            A.append('x')
    else:
        if A[i-K]!='s':
            ans+=S
            A.append('s')
        else:
            A.append('x')

print(ans)