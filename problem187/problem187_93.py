N,X,Y=map(int,input().split())
d=[0]*N
for i in range(N):
    for j in range(N):
        if not i<j:
            continue
        dist=min([j-i,abs((X-1)-i)+1+abs(j-(Y-1))])
        d[dist]+=1
print(*d[1:],sep='\n')