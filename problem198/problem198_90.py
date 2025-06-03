s="abcdefghij"
n=int(input())
ans=[["a",1]]
c=1
while(c<n):
    an=[]
    for i in ans:
        lim=min(i[1]+1,10)
        for j in range(lim):
            if (j==i[1]) and (j!=10):
                an.append([i[0]+s[j],i[1]+1])
            else:
                an.append([i[0]+s[j],i[1]])
    ans=an
    c+=1
for i in ans:
    print(i[0])