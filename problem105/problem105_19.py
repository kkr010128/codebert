n = int(input())
a = list(map(int, input().split()))
ans = 0

for num in range(1, n+1, 2):
    if a[num-1] % 2 != 0:
        ans += 1
print(ans)