n = int(input())
left = []
midplus = []
midzero = []
midminus = []
right = []
L = []
R = []

for i in range(n):
    s = input()
    l = 0
    r = 0
    for x in s:
        if x == '(':
            l += 1
        else:
            if l > 0:
                l -= 1
            else:
                r += 1
    if l > 0 and r == 0:
        left.append((l, r))
    elif l > 0 and r > 0:
        if l > r:
            midplus.append((r, l))  # a,b-a
        elif l == r:
            midzero.append((r,l))
        else:
            midminus.append((r, l))
    elif l == 0 and r > 0:
        right.append((l, r))
    L.append(l)
    R.append(r)

if sum(L) != sum(R):
    print('No')
    exit()

A = 0
B = 0
for x in left:
    A += x[0]
for x in right:
    B += x[1]

midplus = sorted(midplus, key=lambda x: (x[0], -x[1]))
midminus = sorted(midminus, key=lambda x: -x[1])
mid = midplus + midzero + midminus

l = A
r = 0
for a, b in mid:
    if l < a:
        print('No')
        exit()
    l -= a
    l += b

print('Yes')
