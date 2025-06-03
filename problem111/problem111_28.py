import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

lst.sort(reverse = True)

ans = lst[0]
cnt = 0
idx = 1

for _ in range(1, n-1):
    if cnt <= 1:
        ans += lst[idx]
        cnt += 1
    else:
        idx += 1
        cnt = 1
        ans += lst[idx]


print(ans)