n = int(input())
ans = 0
for i in range(1, n):
    if i >= n - i:
        break
    ans += 1
print(ans)