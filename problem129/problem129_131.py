n = int(input())
a = list(map(int, input().split()))
a.sort()
ls = [1] * (10 ** 6 + 1)
cnt = [0] * (10 ** 6 + 1)
for i in range(n):
    cnt[a[i]] += 1
    if cnt[a[i]] == 1:
        if ls[a[i]] == 1:
            for j in range(a[i] * 2, 10 ** 6 + 1, a[i]):
                ls[j] = 0
ans = 0
for i in range(n):
    if ls[a[i]] == 1 and cnt[a[i]] == 1:
        ans += 1
print(ans)
