h = int(input())
w = int(input())
n = int(input())
cnt = 0
ans = 0
while ans < n:
    if h < w:
        ans += w
        h -= 1
    else:
        ans += h
        w -= 1
    cnt += 1
print(cnt)