h, w, k = map(int, input().split())
c = [input() for _ in range(h)]

count = 0
for binh in range(2**h):
    for binw in range(2**w):
        redh, redw = bin(binh)[2:].zfill(h), bin(binw)[2:].zfill(w)  # remove suffix '0x'
        squares = [list(row) for row in c]
        for i, rh in enumerate(redh):
            for wh in range(w):
                if rh == '1':
                    squares[i][wh] = '*'
        for j, rw in enumerate(redw):
            for hw in range(h):
                if rw == '1':
                    squares[hw][j] = '*'
        count += sum(row.count('#') for row in squares) == k

print(count)
