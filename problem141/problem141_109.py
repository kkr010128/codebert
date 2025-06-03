def aaaa():
    n=int(input())
    a=list(map(int, input().split()))
    ans=0
    if a[0]>0:
        if a[0]==1 and n==0:
            return 1
        else:
            return -1
        return -1
    nezen=1
    hazen=0
    line=[]
    liha=[]
    line.append(nezen)
    liha.append(hazen)
    su=0
    su=sum(a[x] for x in range(len(a)))
    for x in range(1,n+1):
        if nezen<=0:
            return -1
        ha=a[x]
        su-=ha
        ne=min(nezen*2-ha,su)
        nezen=ne
        line.append(ne)
        liha.append(ha)
    if line[n]<0:
        return -1
    line[n]=0
    for x in range(len(line)):
        ans+=line[x]+liha[x]
    return ans
print(aaaa())