import bisect
n = int(input())
l = list(map(int,input().split()))
l.sort()
count = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        maxc = l[i]+l[j] #短い2辺の和
        index = bisect.bisect_left(l, maxc)
        if index > j:
            count += index-j-1
print(count)