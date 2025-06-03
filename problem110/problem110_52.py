h, w, f = list(map(int, input().split()))
c = [input() for i in range(h)]
count = 0
bit_h = []
for k in range(2**h):
    hh = []
    for l in range(h):
        if((k >> l) & 1):
            hh.append(1)
        else:
            hh.append(0)
    bit_h.append(hh)

bit_w = []
for i in range(2**w):
    ww = []
    for j in range(w):
        if((i >> j) & 1):
            ww.append(1)
        else:
            ww.append(0)
    bit_w.append(ww)

ans = 0
for i in range(len(bit_h)):
    for j in range(len(bit_w)):
        count = 0
        for k in range(h):
            for l in range(w):
                if bit_h[i][k] == 1 and bit_w[j][l] == 1 and c[k][l] == "#":
                    count += 1
        if count == f:
            ans += 1
print(ans)
