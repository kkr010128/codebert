n=int(input())
s=input()
ans=0
for i in range(n-2):
    if s[i]=="R":
        a,b="G","B"
    elif s[i]=="G":
        a,b="B","R"
    else:
        a,b="R","G"
    cnt=[None]*(n-i-1)
    acnt=0
    bcnt=0
    for j in range(i+1,n):
        if s[j]==a:
            acnt+=1
            cnt[j-i-1]=a
        elif s[j]==b:
            bcnt+=1
            cnt[j-i-1]=b
    tmp=acnt*bcnt
    for j in range((n-i-1)//2):
        if cnt[j]==a and cnt[(j+1)*2-1]==b:
            tmp-=1
        elif cnt[j]==b and cnt[(j+1)*2-1]==a:
            tmp-=1
    ans+=tmp
print(ans)