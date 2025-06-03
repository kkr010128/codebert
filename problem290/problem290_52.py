from collections import Counter
n, k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))
a.sort()
f.sort(reverse=True)

la = 10**6+1
cnt = [0] * la
for u in a:
    cnt[u] += 1
for i in range(1, la):
    cnt[i] += cnt[i-1]


def judge(x):
    y = k
    for i in range(n):
        goal = x//f[i]
        if a[i] > goal:
            y -= a[i] - goal
            if y < 0:
                return False
    return y >= 0


left = -1
right = 10**12 + 1
while left + 1 < right:
    mid = (left + right)//2
    if judge(mid):
        right = mid
    else:
        left = mid

print(right)
