h, w, k = map(int, input().split())

c = [0] * h

for i in range(h):
    c[i] = input()

ans = 0
for rows in range(1 << h):
    for cols in range(1 << w):
        b_cnt = 0
        for _h in range(h+1):
            if not (rows >> _h) & 1:
                continue
            for _w in range(w+1):
                if not (cols >> _w) & 1:
                    continue
                if c[_h][_w] == '#':
                    b_cnt += 1
        if b_cnt == k:
            ans += 1

print(ans)