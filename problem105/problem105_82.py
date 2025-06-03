n = int(input())
a = list(map(int, input().split()))
ans = 0
for i, v in enumerate(a, 1):
    if i % 2 == 1 and v % 2 == 1:
        ans += 1

print(ans)
