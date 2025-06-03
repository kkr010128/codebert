n = int(input())
a = list(map(int, input().split()))
ans = 10 ** 16
a_1 = 0
a_2 = sum(a)
for i in range(n - 1):
    a_1 += a[i]
    a_2 -= a[i]
    ans = min(ans, abs(a_1 - a_2))
print(ans)