n = int(input())
deck = input().split()

bd = list(deck)
for i in range(n):
    for j in reversed(range(i + 1, n)):
        if bd[j][1] < bd[j - 1][1]:
            bd[j], bd[j - 1] = bd[j - 1], bd[j]
print(' '.join(bd))
print('Stable')

sd = list(deck)
for i in range(n):
    mi = i
    for j in range(i, n):
        if sd[j][1] < sd[mi][1]:
            mi = j
    sd[i], sd[mi] = sd[mi], sd[i]
print(' '.join(sd))

if (bd == sd):
    print('Stable')
else:
    print('Not stable')
