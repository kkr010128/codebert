import bisect
n = int(input())
l_li = list(map(int,input().split()))
l_li.sort()
ans = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        ind = bisect.bisect_left(l_li,l_li[i]+l_li[j])
        num = ind-1 - j
        ans += num
print(ans)
