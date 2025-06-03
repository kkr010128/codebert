S = input().strip()
K = int(input())
if K==1 or S[0]!=S[-1]:
    x = list(S)
    cnt = 0
    for i in range(1,len(x)):
        if x[i]==x[i-1]:
            x[i]=0
            cnt += 1
    print(cnt*K)
else:
    x = list(S+S)
    cnt = 0
    for i in range(1,len(x)):
        if x[i]==x[i-1]:
            x[i]=0
            cnt += 1
    k1 = len(x)
    x = x+list(S)
    d1 = 0
    for i in range(k1,len(x)):
        if x[i]==x[i-1]:
            x[i]=0
            d1 += 1
    k2 = len(x)
    x += list(S)
    d2 = d1
    for i in range(k2,len(x)):
        if x[i]==x[i-1]:
            x[i]=0
            d2 += 1
    if K==2:
        print(cnt)
    elif K%2==0:
        print(cnt+d2*(K//2-1))
    else:
        print(cnt+d2*(K//2-1)+d1)