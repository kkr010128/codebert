N,K=map(int,input().split())
P=list(map(int,input().split()))
C=list(map(int,input().split()))
ans=[]
for i in range(N):
    score=[]
    B=[]
    count=1
    nex=P[i]-1
    point=C[nex]
    B.append(C[nex])
    score.append(point)
    while count<=K:
        if nex==i:
            break
        nex=P[nex]-1
        point+=C[nex]
        score.append(point)
        B.append(C[nex])
        count+=1
    if count==K:
        ans.append(max(score))
    else:
        if point<=0:
            ans.append(max(score))
        else:
            a=K//count
            b=K%count
            maxpoint=point*(a-1)
            for j in range(b):
                maxpoint+=B[j]
            c=maxpoint
            for j in range(count):
                if b+j<count:
                    c+=B[b+j]
                else:
                    c+=B[b+j-count]
                maxpoint=max(maxpoint,c)
            ans.append(maxpoint)
print(max(ans))