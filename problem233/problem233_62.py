n, *aa = map(int, open(0).read().split())
# aa = aa
bb = []

tmp = aa[0]
for a in aa:
    tmp = min(a,tmp)
    bb.append(tmp)

# bb = bb[:-1]

print(sum([a<=b for a, b in zip(aa, bb)]))