A=[]
for _ in range(3):
    A+=map(int,input().split())

N=int(input())
for _ in range(N):
    b=int(input())
    if b in A:
        A[A.index(b)]=0

for i,j,k in [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6),
]:
    if A[i]==A[j]==A[k]:
        print('Yes')
        break
else:
    print('No')
