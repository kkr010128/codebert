n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7

ans = 0
for keta in range(61):
    now = 0
    for x in a:
        if x & (1 << keta):
            now += 1
    ans += (now*(n-now))*2**keta
    ans %= mod

print(ans)
