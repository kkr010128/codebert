h, w = map(int, input().split())
s_list = []  # h, w
dp_dict = {}
for i in range(h):
    s = input()
    temp_list = []
    for temp in s:
        if temp == "#":
            temp_list.append(1)
        else:
            temp_list.append(0)
    s_list.append(temp_list)


def search(x, y, black):
    res = 0
    if (x, y, black) in dp_dict:
        return dp_dict[(x, y, black)]
    if x == w-1 and y == h-1:
        if s_list[y][x] == 1:
            if black:
                res = 0
            else:
                res = 1
        else:
            res = 0
    elif x == w-1:
        if s_list[y][x] == 1:
            if black:
                res = search(x, y+1, True)
            else:
                res = search(x, y+1, True)+1
        else:
            res = search(x, y+1, False)
    elif y == h-1:
        if s_list[y][x] == 1:
            if black:
                res = search(x+1, y, True)
            else:
                res = search(x+1, y, True)+1
        else:
            res = search(x+1, y, False)
    else:
        if s_list[y][x] == 1:
            if black:
                res = min([search(x+1, y, True), search(x, y+1, True)])
            else:
                res = min([search(x+1, y, True), search(x, y+1, True)])+1
        else:
            res = min([search(x+1, y, False), search(x, y+1, False)])
    dp_dict[(x, y, black)] = res
    return res


print(search(0, 0, False))
