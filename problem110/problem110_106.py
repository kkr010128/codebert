def make_bit(n):
    bit = []
    for i in range(2**n):
        bit.append(bin(i)[2::])
    i = 0
    while i < len(bit):
        while len(bit[i]) < len(bin(2**n-1)[2::]):
            bit[i] = "0" + bit[i]
        i += 1

    return bit

h, w, k = map(int, input().split())

c = [list(input()) for _ in range(h)]

h_pats = make_bit(h)
w_pats = make_bit(w)
ans = 0
for h_pat in h_pats:
    for w_pat in w_pats:
        cnt = 0
        for i in range(h):
            for j in range(w):
                if h_pat[i] == "1" or w_pat[j] == "1":
                    continue
                if c[i][j] == "#":
                    cnt += 1
        if cnt == k:
            ans += 1

print(ans)