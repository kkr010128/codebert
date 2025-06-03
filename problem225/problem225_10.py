h, a = map(int, input().split())
ans = 0
while True:
    if h > 0:
        h = h - a
        ans += 1
    else:
        print(ans)
        exit()
