n,k =  map(int,input().split())
A = list(map(int,input().split()))

l = min(A)//(k+1) 
r = max(A)
m = (l+r)//2+1

while 1:
    
    m = (l+r)//2
    if m==0:
        m=1
        break

    
    #m以下の長さにできるか判定
    
    # A_long = A[A>m]
    n= sum( [  int((A[i]-0.1)//(m)) for i in range(len(A)) ] )
    
    # print(l,m,r,n)
    
    if n<=k:
        if r==m:
            break
        r=m-1
    else:
        if l==m:
            m+=1
            break
        l=m+1
        

        
print(m)