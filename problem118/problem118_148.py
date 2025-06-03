n = int(input())

cnt = [1] * (n + 1)
cnt[0] = 0
cnt[1] = 0

p = 2
while p  <= n // 2:
    for i in range(p*2, n+1, p):
        cnt[i] += 1
    p += 1

ans = 0
for i in range(1, n+1):
    # print(i, cnt[i]+1)
    ans += i * (cnt[i] + 1)

print(ans)

