import sys
n=int(input())
a=input()
a=[int(s)for s in a.split()]
M=1
Q=1
m=sum(a)
if a[0]>=1:
    if a[0]==1 and n==0:
        print(1)
        sys.exit()
    else:    
        print(-1)
        sys.exit()
for i in range(n):
    M=2*M-a[i+1]
    if M<0:
        print(-1)
        sys.exit()
    M1=M+a[i+1]
    m=m-a[i]
    Q=Q+min(M1,m)
print(Q)