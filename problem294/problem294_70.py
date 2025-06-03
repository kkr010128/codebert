import bisect

n = int(input())
l = list(map(int, input().split()))
l.sort()
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if j == n-1:
            continue
        x = l[i] + l[j]
        cnt += bisect.bisect_left(l[j+1:], x)
print(cnt)