n = int(input())
a = list(map(int, input().split()))
ans = 0
tallest = 0
for i in range(n):
    tallest = max(tallest, a[i])
    ans += tallest - a[i]
print(int(ans))
