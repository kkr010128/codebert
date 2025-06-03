n, h = map(int, input().split())
hn = map(int, input().split())
cnt = 0
for i in hn:
    if i >= h:
        cnt += 1
print(cnt)