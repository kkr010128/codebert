h = int(input())

ans = 0
cnt = 1
while h > 1:
    ans += cnt
    h /= 2
    cnt = cnt * 2
if int(h) == 1:
    ans += cnt

print(ans)