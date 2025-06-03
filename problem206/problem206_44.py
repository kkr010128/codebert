n = int(input())

ans = n // 2
ans += 1 if n % 2 != 0 else 0

print(ans)