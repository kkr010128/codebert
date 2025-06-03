# encoding:utf-8

def set_char(data):
    if data[len(data)-1] == "#":
        return "."
    else:
        return "#"

while True:
    str_line_1 = "#"
    str_line_2 = "."

    H ,W = map(int, input().split(" "))

    if H == W == 0:
        break

    for i in range(W - 1):
        str_line_1 += set_char(str_line_1)
        str_line_2 += set_char(str_line_2)

    for i in range(H):
        if (i % 2) == 0:
            print(str_line_1)
        else:
            print(str_line_2)
    print()