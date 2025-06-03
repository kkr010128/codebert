def up(mtx, i, j, val):
    h = i - 1
    if h < 0:
        return
    elif mtx[h][j] != 0:
        return
    else:
        mtx[h][j] = val
        up(mtx, h, j, val)


def down(mtx, i, j, val):
    h = i + 1
    if h >= len(mtx):
        return
    elif mtx[h][j] != 0:
        return
    else:
        mtx[h][j] = val
        down(mtx, h, j, val)


h, w, k = map(int, input().split())

mtx = []

for i in range(h):
    s = input()
    s_list = []
    for j in range(len(s)):
        if s[j] == "#":
            s_list.append(1)
        else:
            s_list.append(0)
    mtx.append(s_list)

ret = [[0] * w for i in range(h)]

ptr = 1

for i in range(h):
    cnt = mtx[i].count(1)
    if cnt == 0:
        continue
    else:
        is_first = True
        for j in range(w):
            if mtx[i][j] == 0:
                ret[i][j] = ptr
            else:
                if is_first:
                    ret[i][j] = ptr
                    is_first = False
                else:
                    ptr += 1
                    ret[i][j] = ptr
        ptr += 1

for i in range(h):
    for j in range(w):
        if ret[i][j] != 0:
            up(ret, i, j, ret[i][j])
            down(ret, i, j, ret[i][j])

for i in range(h):
    print(" ".join(list(map(str, ret[i]))))
