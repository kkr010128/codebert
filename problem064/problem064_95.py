n=str(input())
a=len(n)
N=list(n)
m=str(input())
A=len(m)
x=0
for i in range(a):
    C=[]
    for i in range(A):
        C.append(N[i])
    B=''.join(C)
    c=N[0]
    if B==m:
        x=x+1
    N.remove(c)
    N.append(c)
if x>0:
    print('Yes')
else:
    print('No')
        
    
