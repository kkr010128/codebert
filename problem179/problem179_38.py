N,M=map(int,input().split())
A=[int(x) for x in input().split()]
s=sum(A)
l=len(A)
m=0
for i in range(l):
    if A[i]>=s/(4*M):
        m+=1
if M<=m:
    print('Yes')
else:
    print('No')