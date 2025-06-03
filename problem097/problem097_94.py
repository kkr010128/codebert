K = int(input())
if K%2==0:
    print(-1)
elif K==1:
    print(1)
elif K==7:
    print(1)
else:
    if K%7==0:
        K = K//7
    a = 1
    cnt = 1
    ind = -1
    for i in range(K):
        a = (a*10)%K
        cnt += a
        if cnt%K==0:
            ind = i
            break
    if ind<0:
        print(-1)
    else:
        print(ind+2)