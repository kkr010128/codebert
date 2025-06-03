n = int(input())
a = list(map(int, input().split()))

cnt = [0] * (10 ** 6 + 1)

for i in range(n):
    cnt[a[i]] += 1

a_uniq = []

for i in range(10 ** 6 + 1):
    if cnt[i] == 1:
        a_uniq.append(i)

cnt = [0] * (10 ** 6 + 1)

for i in list(set(a)):
    for j in range(2 * i, 10 ** 6 + 1, i):
        cnt[j] = 1

ans = 0

for i in a_uniq:
    if cnt[i] == 0:
        ans += 1

print(ans)