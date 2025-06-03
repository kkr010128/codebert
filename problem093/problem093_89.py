n,k = map(int,input().split())
p = [int(i)-1 for i in input().split()]
c = [int(i) for i in input().split()]

ans = -10**100

for i in range(n):
    chk = [0]*n
    chk[p[i]] = 1
    now = p[i]
    cnt = 1
    val = [-10**100]*n
    val[0] = c[p[i]]
    while 1 == 1:
        if cnt >= k:
            break
        #print(p[now])
        if chk[p[now]] == 1:
            break
        else:
            chk[p[now]] = 1
            val[cnt] = val[cnt-1]+c[p[now]]
            now = p[now]
            cnt += 1
    
    cnt -= 1
    
    #print(val)
    
    if val[cnt] <= 0:
        ans = max(ans,max(val))
    else:
        num = k // (cnt+1)
        amari = k % (cnt+1)
        #print(cnt,k)
        for j in range(cnt+1):
            if j < amari:
                tmp = num*val[cnt]
            else:
                tmp = (num-1)*val[cnt]
            ans = max(ans,tmp+val[j])
            #print(ans,tmp,val[j],j,cnt,num)
    
    #ans = max(ans,max(val))
    
print(ans)