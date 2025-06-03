n = int(input())

ans = 0
for a in range(1,n):
    b = n//a
    if b*a == n:
        b -= 1
    ans += b
print(ans)