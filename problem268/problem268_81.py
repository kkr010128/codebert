n = int(input())
a = list(map(int, input().split()))

mod = 10**9 + 7
ans = 1
cnt = [0] * 3
for i in range(n):
    t = 0
    first = True
    for j in range(3):
        if cnt[j] == a[i]:
            t += 1
            if first:
                first = False
                cnt[j] += 1
    ans = (ans * t) % mod
print(ans)