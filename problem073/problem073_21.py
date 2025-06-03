n = int(input())
ans = 0
for a in range (1,n):
    for b in range(1, n):
        if n <= a * b:
            break
        ans += 1
print(ans)