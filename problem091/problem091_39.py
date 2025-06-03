n = int(input())
l = list(map(int, input().split()))
r = {l[i]:0 for i in range(n)}
for i in range(n):
    r[l[i]] += 1
t = list(r.items())
ans = 0
for i in range(len(t)-2):
    for j in range(i+1, len(t)-1):
        for k in range(j+1, len(t)):
            y = sum([t[i][0], t[j][0], t[k][0]])
            x = max([t[i][0], t[j][0], t[k][0]])
            if 2*x < y:
                ans += t[i][1] * t[j][1] * t[k][1]
print(ans)