import bisect

n = int(input())
l = list(map(int, input().split()))
ans = 0
l.sort()

for i in range(n-2):
    for j in range(i+1, n-1):
        c_i = bisect.bisect_left(l, l[i]+l[j])
        if c_i > j:
            ans += c_i - j - 1
        else:
            continue
print(ans)