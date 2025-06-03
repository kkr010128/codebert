n=int(input())
l=sorted(list(map(int, input().split())))

ans=0
for i in range(len(l)):
    for j in range(i+1, len(l)):
        for k in range(j+1, len(l)):
            if l[i]==l[j] or l[j]==l[k] or l[k]==l[i]:
                continue
            if l[i]+l[j]>l[k]:
                ans+=1
print(ans)