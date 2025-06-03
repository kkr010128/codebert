N=int(input())



div=10**9+7
def po(x,n,M):
    res=1
    if n>0:
        
        res= po(x,n//2,M)
    if n%2==0:
        res=(res*res)%M
    else:
        res=(((res*res)%M)*x)%M
        
      
    return res

A=po(10,N,div)
B=po(9,N,div)
C=po(8,N,div)
ans=(A-2*B+C)%div
print(ans)