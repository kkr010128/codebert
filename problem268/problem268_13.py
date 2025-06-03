N = int(input())
*A, = map(int, input().split())
mod = 10**9 + 7

ans = 1
cnt = [0, 0, 0]
for a in A:
    if a not in cnt:
        ans = 0
        break
    ans = ans * cnt.count(a) % mod
    cnt[cnt.index(a)] += 1
print(ans)
