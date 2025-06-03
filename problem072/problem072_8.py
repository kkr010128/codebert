N=int(input())
A=[]
for i in range(N):
    D=list(map(int,input().split()))
    A.append(D)
    
for i in range(N-2):
    if A[i][0]==A[i][1] and A[i+1][0]==A[i+1][1] and A[i+2][0]==A[i+2][1]:
        print('Yes')
        break
else:
    print('No')