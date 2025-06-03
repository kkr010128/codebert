import bisect
n = int(input())
ls = list(map(int,input().split()))
ls = sorted(ls)
ans = 0
for i in range(n):
    for j in range(i+1,n):
        k = bisect.bisect_left(ls,ls[i]+ls[j])
        ans += k-j-1
print(ans)