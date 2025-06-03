n=int(input())
llist=list(map(int,input().split()))
ans=0
for i in range(n):
    for j in range(n-i-1):
        for k in range(n-i-j-2):
            ii=llist[i]
            ji=llist[i+j+1]
            ki=llist[i+j+k+2]
            if ji != ii and ji != ki and ii != ki:
                if max(ii,ji,ki)*2 < ji+ii+ki:
                    ans+=1

print(ans)