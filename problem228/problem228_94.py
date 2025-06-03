H = int(input())

ans = 0
cnt = 0
while True:
    ans += 2 ** cnt
    if H == 1:
        break
    H = H//2
    cnt += 1

print(ans)