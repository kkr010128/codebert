n = int(input())

ans = 0
for i in range(1, n):
    ans += n//i if n%i != 0 else n//i-1

print(ans)
