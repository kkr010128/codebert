n=int(input())
a=list(map(int,input().split()))

#R,B,Gの順に埋めていく
#R,B,Gの現在の数を保存する
cnt={'R':0,'B':0,'G':0}
ans=1
for i in range(n):
    count=0
    edi=0
    for j in 'RBG':
        if cnt[j]==a[i]:
            count+=1
            if edi==0:
                cnt[j]+=1
                edi=1
    ans*=count
print(ans%(10**9+7))