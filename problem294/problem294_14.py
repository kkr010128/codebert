import bisect
n=int(input())
a=sorted(list(map(int,input().split())))
cnt=0
for i in range(n):
    for j in range(i+1,n):
        cnt+=bisect.bisect_left(a,a[i]+a[j])-(j+1)
print(cnt)