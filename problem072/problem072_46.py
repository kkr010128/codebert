n=int(input())
count=0
maxs=0
for _ in range(n):
    d1,d2=map(int,input().split())
    if d1==d2:
        count+=1
    else:
        maxs=max(maxs,count)
        count=0

maxs=max(count,maxs)
if maxs>=3:
    print("Yes")
else:
    print("No")