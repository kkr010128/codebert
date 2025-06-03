weatherS = input()
p = weatherS[0] == 'R'
q = weatherS[1] == 'R'
r = weatherS[2] == 'R'

if p and q and r:
    serial = 3
elif (p and q) or (q and r):
    serial = 2
elif p or q or r:
    serial = 1
else:
    serial = 0

print(serial)