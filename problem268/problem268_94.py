n = int(input())
hats = list(map(int, input().split()))

mod = 1000000007

cnt = [0] * 3
ans = 1

for i in range(n):
    count = 0
    minj = 4
    for j in range(3):
        if hats[i] == cnt[j]:
            count += 1
            minj = min(minj, j)
    if count == 0:
        ans = 0
        break
    cnt[minj] += 1

    ans = ans * count % mod

print(ans)