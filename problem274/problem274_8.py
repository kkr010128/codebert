n, m = map(int, input().split())
s = input()

if "1" * m in s:
    print(-1)
    exit()

pos = n
ans = []
while pos > 0:
    prev = max(pos - m, 0)
    while s[prev] == "1":
        prev += 1

    ans.append(pos - prev)

    pos = prev

ans = ans[::-1]
print(*ans)
