n = int(input())
a = list(map(int, input().split()))
r, cnt = 1, 0
for i in a:
    if r == i:
        r += 1
    else:
        cnt += 1

print(cnt) if a.count(1) else print(-1)
