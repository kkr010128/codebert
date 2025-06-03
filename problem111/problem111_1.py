n = int(input())
a = sorted(list(map(int, input().split())))
ans = a.pop()
if n % 2:
    for i in range((n - 2) // 2):
        ans += a.pop() * 2
    ans += a.pop()
    print(ans)
else:
    for i in range((n - 2) // 2):
        ans += a.pop() * 2
    print(ans)