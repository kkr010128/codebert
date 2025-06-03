a, b, c = list(map(int, input().split()))
ans = 0
for i in range(a, b+1):
    if i == 1 or c % i == 0:
        ans += 1
print(ans)