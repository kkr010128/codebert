n = int(input())

ans = 0
if n >= 2 and n % 2 == 0:
    j = 10
    while n >= j:
        ans += (n // j)
        j *= 5

print(ans)