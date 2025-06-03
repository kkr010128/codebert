n=int(input())
lst=list(map(int,input().split()))
tmp=0
for i in range(n):
    if tmp+1==lst[i]:
        tmp+=1
print(n-tmp if tmp>0 else -1)