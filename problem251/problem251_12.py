n,k=map(int,input().split())

r,s,p = map(int,input().split())

T=list(input())

a=[[] for i in range(k)]

for i in range(n):
    a[i%k].append(T[i])


score=0
for j in range(k):
    b=a[j]
    flg=0
    for l in range(len(b)):
        if l==0:
            if b[l]=='r':
                score+=p
            elif b[l]=='s':
                score+=r
            elif b[l]=='p':
                score+=s
        else:
            if b[l-1]==b[l] and flg==0:
                flg=1
                continue
            elif b[l-1]==b[l] and flg==1:
                if b[l]=='r':
                    score+=p
                elif b[l]=='s':
                    score+=r
                elif b[l]=='p':
                    score+=s
                flg=0
            elif b[l-1]!=b[l]:
                if b[l]=='r':
                    score+=p
                elif b[l]=='s':
                    score+=r
                elif b[l]=='p':
                    score+=s
                flg=0

print(score)


