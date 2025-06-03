N=int(input())
S=input()
code=list(set(list(S)))
ans=0
for i in code:
    for j in code:
        for k in code:
            count=0
            for s in S:
                if count==0:
                    if s==i:
                        count+=1
                elif count==1:
                    if s==j:
                        count+=1
                elif count==2:
                    if s==k:
                        count+=1
                if count==3:
                    ans+=1
                    break
print(ans)