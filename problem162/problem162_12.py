n,m=map(int,input().split())
if n%2==1:
    for i in range(m):
        print(i+1, n-i-1)
else:
    used = [False]*n
    next = [i+1 for i in range(m)][::-2]+[i+1 for i in range(m)][-2::-2]
    i=0
    now=0
    count=0
    while True:
        if used[now]==False and used[now+next[i]]==False:
            print(now+1, now+next[i]+1)
            count+=1
            if count==m:
                break
            used[now]=True
            used[now+next[i]]=True
            i+=1
            now+=1
        else:
            now+=1