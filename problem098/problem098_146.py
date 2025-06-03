n = int(input())
c = input()

t = n
lw, rr = 0, c.count('R')
for ci in c+'Z':
    swap = min(lw, rr)
    wtor, rtow = max(0, lw-swap), max(0, rr-swap)
    t = min(t, swap + wtor + rtow)
    lw = lw + (ci == 'W')
    rr = rr - (ci == 'R')

print(t)
