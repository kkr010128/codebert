X,Y,A,B,C=list(map(int,input().split()))
p=sorted(list(map(int,input().split())),reverse=True)
q=sorted(list(map(int,input().split())),reverse=True)
r=sorted(list(map(int,input().split())),reverse=True)

i=X-1
j=Y-1
k=0

ans=sum(p[:X])+sum(q[:Y])

while k<len(r):
    if i>-1 and j>-1:
        if p[i]<q[j]:
            cmin=p[i]
            i-=1
        else:
            cmin=q[j]
            j-=1
        
        if r[k]<=cmin:
            break
        ans+=r[k]-cmin
        k+=1
    elif i>-1:
        cmin=p[i]
        i-=1

        if r[k]<=cmin:
            break

        ans+=r[k]-cmin
        k+=1
    elif j>-1:
        cmin=q[j]
        j-=1

        if r[k]<=cmin:
            break

        ans+=r[k]-cmin
        k+=1
    else:
        break

print(ans)
