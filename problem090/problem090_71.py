S = input()

mx = 0
c = 0
for si in S:
    if si == 'R':
        c += 1
        mx = max(mx, c)
    else:
        c = 0

print(mx)