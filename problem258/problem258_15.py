n = int(input())

ans = 0
if n%2 == 0:
    i = 10
    while i <= n:
        ans += n//i
        i *= 5

print(ans)

