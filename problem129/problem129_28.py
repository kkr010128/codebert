n = int(input())
a = list(map(int, input().split()))
a.sort()
m = a[-1]
c = [0] * (m + 1)

for ai in a:
    for i in range(ai, m + 1, ai):
        c[i] += 1

ans = 0
for ai in a:
    if c[ai] == 1:
        ans += c[ai]

print(ans)