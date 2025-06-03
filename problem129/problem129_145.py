n = int(input())
a = list(map(int, input().split()))
cnt = [0] * (10 ** 6 + 1)
a.sort()
ans = 0


for i in a:
    cnt[i] += 1

a = set(a)

for k in a:
    for l in range(k * 2, (10 ** 6 + 1), k):
        cnt[l] += 1

for m in a:
    if cnt[m] == 1:
        ans += 1
    


print(ans)