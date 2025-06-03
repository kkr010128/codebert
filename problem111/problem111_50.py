n = int(input())
a = [int(i) for i in input().split()]
a.sort(reverse=True)
i = 1
ans = a[0]
c = 1
while c < n - 1:
    k = min(2, n - 1 - c)
    c += k
    ans += a[i] * k
    i += 1
print(ans)
