n = int(input())
c = {}
m = 0
for i in range(n):
    s = input()
    if s in c:
        c[s] += 1
    else:
        c[s] = 1
    if m < c[s]:
        m = c[s]

ans = []

for i in c:
    if m == c[i]:
        ans.append(i)

ans = sorted(ans)

for i in ans:
    print(i)
