res_list = [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]

n = int(input())

for i in range(n):
    io_rec = list(map(int, input().split(" ")))
    bld_num = io_rec[0] - 1
    floor_num = io_rec[1] - 1
    room_num = io_rec[2] - 1
    io_headcnt = io_rec[3]
    res_list[bld_num][floor_num][room_num] += io_headcnt


for i in range(4):
    if i:
        print("#" * 20)
    bld = res_list[i]
    for j in bld:
        floor_str = map(str, j)
        print(" " + " ".join(floor_str))