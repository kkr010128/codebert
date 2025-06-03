n, m = map(int, input().split())
ac = [0]*n
wa = [0]*n
for _ in range(m):
    p, s = input().split()
    p = int(p)-1
    if s == 'AC':
        ac[p] = 1
    elif s == 'WA' and ac[p] == 0:
        wa[p] += 1

ans, pen = 0, 0
for i in range(n):
    if ac[i]:
        ans += 1
        pen += wa[i]
print(ans, pen)