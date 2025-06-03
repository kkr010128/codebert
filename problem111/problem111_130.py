n = int(input())
a = sorted(map(int, input().split()), reverse=True)

ans, que, cnt = 0, [a[0]], 0
for i in a[1:]:
    ans += que[cnt]
    que += [i, i]
    cnt += 1
print(ans)
