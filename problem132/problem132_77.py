n,k=map(int,input().split())
A=list(map(int,input().split()))

def culc(L):
    subL=[0]*(n+1)

    for i in range(n):
        temp=L[i]
        bottom=max(i-temp,0)
        top=min(i+temp,n-1)

        subL[bottom]+=1
        subL[top+1]-=1
    
    resL=[0]*n
    resL[0]=subL[0]
    for i in range(1,n):
        resL[i]=resL[i-1]+subL[i]

    return resL

for i in range(min(k,41)):
    A=culc(A)

print(*A)
