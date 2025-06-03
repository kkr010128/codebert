n, m = map(int, input().split())
ac = [0] * n
wa = [0] * n
for _ in range(m):
    p, s = input().split()
    if s == 'AC':
        ac[int(p) - 1] = 1
    elif ac[int(p) - 1] == 0:
        wa[int(p) - 1] += 1
for i in range(n):
    if ac[i] == 0:
        wa[i] = 0
print(sum(ac), sum(wa))