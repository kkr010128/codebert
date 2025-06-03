import bisect
n = int(input())
l = list(map(int, input().split()))
sort_l = sorted(l)
count = 0

for a in range(n):
    for b in range(a+1, n):
        c = bisect.bisect_left(sort_l, sort_l[a] + sort_l[b])
        if c > b:
            count += c - b -1
        else:
            pass     
        

print(count)