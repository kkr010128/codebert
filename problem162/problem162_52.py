N,M=map(int,input().split())
venue=[]
if N%2==0:
    l=1
    r=N//2
    while l<r:
        venue.append([l,r])
        l+=1
        r-=1
    l=N//2+1
    r=N-1
    while l<r:
        venue.append([l,r])
        l+=1
        r-=1
else:
    l=1
    r=N//2
    while l<r:
        venue.append([l,r])
        l+=1
        r-=1
    l=N//2+1
    r=N
    while l<r:
        venue.append([l,r])
        l+=1
        r-=1
for a,b in venue:
    M-=1
    print(a,b)
    if M==0:
        break
