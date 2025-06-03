B=[]
for i in range(3):
    A=list(map(int,input().split()))
    B.append(A[0])
    B.append(A[1])
    B.append(A[2])
N=int(input())
for j in range(N):
    b=int(input())
    if b in B:
        B[B.index(b)]=0
if B[0]==0 and B[1]==0 and B[2]==0:
    print('Yes')
elif B[3]==0 and B[4]==0 and B[5]==0:
    print('Yes')
elif B[6]==0 and B[7]==0 and B[8]==0:
    print('Yes')
elif B[0]==0 and B[3]==0 and B[6]==0:
    print('Yes')
elif B[1]==0 and B[4]==0 and B[7]==0:
    print('Yes')
elif B[2]==0 and B[5]==0 and B[8]==0:
    print('Yes')
elif B[0]==0 and B[4]==0 and B[8]==0:
    print('Yes')
elif B[2]==0 and B[4]==0 and B[6]==0:
    print('Yes')
else:
    print('No')