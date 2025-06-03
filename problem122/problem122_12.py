N=int(input())
A=list(map(int, input().split()))
q=int(input())
Q=[list(map(int, input().split())) for _ in range(q)]

L=[0]*(10**5+1)
S=0
for i in range(N):
    L[A[i]]+=1
    S+=A[i]

for i in range(q):
    S+=L[Q[i][0]]*(Q[i][1]-Q[i][0])
    L[Q[i][1]]+=L[Q[i][0]]
    L[Q[i][0]]=0
    # print(L)
    print(S)