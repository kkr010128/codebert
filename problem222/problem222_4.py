n=int(input())
a=[int(i) for i in input().split()]
cnt={}
for i in range(n):
    cnt[a[i]]=0
ok=1
for i in range(n):
    cnt[a[i]]+=1
    if cnt[a[i]]==2:
        print("NO")
        ok=0
        break
if ok==1:
    print("YES")

