


nk=input().split()

n=int(nk[0])
k=int(nk[1])

weight=[int(input()) for i in range(n)]

def ok(m):
    load=0
    track=1
    # sum all the weight and count the track number we need
    for i in range(n):
        load+=weight[i]
        if load==m:
            load=0
            if i!=n-1:
                track+=1
        elif load>m:
            if weight[i]>m:
                return False
            else:
                load=weight[i]
                track+=1
        else:
            continue

    if track<=k:
        return True
    else:
        return False

low=0
high=sum(weight)
while low+1<high:
# low<mid<high
#not ok(l) and ok(h)
    mid=(low+high)//2
    if ok(mid):
        high=mid
    else:
        low=mid


print(high)