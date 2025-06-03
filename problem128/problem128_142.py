X,N = map(int,input().split())
p = [int(i) for i in input().split()]
if N==0:
    print(X)
else:
    pN=[]
    for j in range(N):
        pj = p[j]-X
        pN.append(pj)
    pN.sort()
    p0 = pN[0]-1
    p1 = pN[N-1]+1
    list_p = list(range(p0,p1+1,1))
    result = list(set(list_p)-set(pN))
    k0 = abs(result[0])
    for k in result:
        k1 = abs(k)
        if k1<k0:
            k0 = k1
    cnt = 0
    for l in result:
        if l == (-1)*k0:
            cnt+=1
    if cnt==0:
        print(X+k0)
    else:
        print(X-k0)