import bisect

n, m, k = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

for i in range(len(alist)-1):
    alist[i+1] += alist[i]

for i in range(len(blist)-1):
    blist[i+1] += blist[i]

x = bisect.bisect_right(alist, k)
ans = bisect.bisect_right(blist, k)
for i in range(x):
    d = k - alist[i]
    y = bisect.bisect_right(blist, d) + i + 1
    if ans < y:
        ans = y

print(ans)