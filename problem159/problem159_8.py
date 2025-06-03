x = int(input())
n = 100
ans = 0
while (x > n):
    n += (n//100)
    ans += 1
print(ans)