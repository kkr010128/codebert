#coding:UTF-8
def FN(n):
    if n==0 or n==1:
        F[n]=1
        return F[n]
    if F[n]!=None:
        return F[n]
    F[n]=FN(n-1)+FN(n-2)
    return F[n]

if __name__=="__main__":
    n=int(input())
    F=[None]*(n+1)
    ans=FN(n)
    print(ans)