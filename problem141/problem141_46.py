n=int(input())
a=list(map(int,input().split()))
if a[0]>=2:
    print(-1)

else:
    pN=1
    s=1
    l=[]
    S=sum(a)
    b=0
    z=1
    for k in range(len(a)):
        b+=a[k]
        l.append(b)

    for i in range(1,n+1):
        if a[i]>2*pN:
            print(-1)
            z=0
            break
        else:
            pN=min(2*pN-a[i],S-l[i])
            s+=pN
    s+=S
    if n==0:
        s=1
    if a[0]==1 and n>=1:
            print(-1)
            z=0

    if z:
        print(s)