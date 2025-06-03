A=[[int(n) for n in input().split()] for m in range(3)]
N=int(input())

for i in range(N):
    b=int(input())
    for j in range(3):
        for k in range(3):
            if b==A[j][k]:
                A[j][k]=0
                
ans="No"

for i in range(3):
    if A[i][0]==0 and A[i][1]==0 and A[i][2]==0:
        ans="Yes"

for i in range(3):
    if  A[0][i]==0 and A[1][i]==0 and A[2][i]==0: 
        ans="Yes"

if (A[0][0]==0 and A[1][1]==0 and A[2][2]==0) or (A[0][2]==0 and A[1][1]==0 and A[2][0]==0):
    ans="Yes"


print(ans)

