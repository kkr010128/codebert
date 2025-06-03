n, m = map(int, input().split())
prob = [0]*n
AC = 0
WA = 0
for _ in range(m):
    p, s = input().split()
    p = int(p)
    if prob[p-1] == -1:
        continue
    if s == 'WA':
        prob[p-1] += 1
    else:
        WA += prob[p-1]
        AC += 1
        prob[p-1] = -1
print(AC, WA)
