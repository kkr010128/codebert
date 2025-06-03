N=int(input())
ans=0
speech_l=[[] for _ in range(N)]
for i in range(N):
    tmp=int(input())
    for j in range(tmp):
        speech_l[i].append(list(map(int,input().split())))
for i in range(2**N):
    sw=0
    l=[1]*N
    tmp=N
    for j in range(N):
        if ((i >> j)&1):
            tmp-=1
            l[j]=0
    for j in range(N):
        if l[j] == 1:
            for k in speech_l[j]:
                if l[k[0]-1] != k[1]:
                    sw=1
    if sw==0:
        ans=max(ans,tmp)
print(ans)