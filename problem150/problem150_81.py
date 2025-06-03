n,k=map(int,input().split())
A = list(map(int,input().split()))

C=[0]*n
C[0]=1
c=0
loopc=0
i=0
io=0
while c<k :
    newi = A[i]-1
    C[newi]+=1
    if C[newi]>=3 :
        rs=newi
        break
    elif C[newi]==2 :
        loopc+=1
    io=i
    i=newi
    c+=1

if (k-c)<0 or loopc==0 :
    print(i+1)
    exit()
mod = (k-c)%(loopc)
# print( k, c, loopc, i, mod)


# i=rs
while mod>0 :
    newi = A[i]-1
    i=newi
    mod-=1

print( i+1 )
