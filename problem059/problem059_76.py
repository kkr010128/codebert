(r, c) = [int(i) for i in input().split()]

ct = [0 for d in range(c)]
tmp = []
for rc in range(r):
    tmp = [int(i) for i in input().split()]
    total = 0
    for cc in range(c):
        ct[cc] += tmp[cc]
        total += tmp[cc]
        print(tmp[cc], end=' ')
    print(total)
total = sum(ct)
print(' '.join([str(i) for i in ct]), total)