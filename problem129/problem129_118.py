n = int(input())
a = list(map(int, input().split()))

f = [0 for i in range(10**6+5)]
for x in a:
    f[x] += 1
for i in range(1, len(f)):
    if f[i] == 0:
        continue
    for j in range(2*i, len(f), i):
        f[j] = 0
ans = 0
for v in f:
    if v == 1:
        ans += 1
print(ans)
