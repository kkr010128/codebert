n, m = map(int, input().split())
wa = [0] * n
ac = [False] * n

for i in range(m):
    p, s = input().split()
    p = int(p) - 1
    if s == 'WA' and not ac[p]:
        wa[p] += 1
    elif s == 'AC':
        ac[p] = True

wa_n = sum(wa[i] if ac[i] else 0 for i in range(n))
print("{} {}".format(sum(ac), wa_n))