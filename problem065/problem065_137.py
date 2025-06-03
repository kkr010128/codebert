W = input().lower()
ans = 0
while True:
    s = input()

    if s == "END_OF_TEXT":
        break

    s = s.lower().split()

    ans += s.count(W)

print(ans)
