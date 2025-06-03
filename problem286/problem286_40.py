a, b = map(int, input().split())

if (a < 10):
    if (b < 10):
        ans = a * b
    else:
        ans = -1
else:
    ans = -1

print(ans)