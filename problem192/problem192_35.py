from math import factorial
n=int(input())
cnt=[0]*(n+1)
lst=list(map(int,input().split()))
for i in lst:
    cnt[i]+=1
ans=0
for i in range(n+1):
    p=cnt[i]
    if p>=2:
        ans+=factorial(p)//factorial(p-2)//2
for i in range(n):
    print(ans-cnt[lst[i]]+1)