import numpy as np
import itertools as it

H,W,N = [int(i) for i in input().split()]
dat = np.array([list(input()) for i in range(H)], dtype=str)


emp_r = ["." for i in range(W)]
emp_c = ["." for i in range(H)]


def plot(dat, dict):
    for y in dict["row"]:
        dat[y,:] = emp_r
    for x in dict["col"]:
        dat[:,x] = emp_c
    return dat


def is_sat(dat):
    count = 0
    for y in range(W):
        for x in range(H):
            if dat[x, y] == "#":
                count += 1

    if count == N:
        return True
    else:
        return False

# def get_one_idx(bi, digit_num):
#     tmp = []
#     for j in range(digit_num):
#         if (bi >> j) == 1:
#             tmp.append()



# plot(dat, dict={"row": [], "col":[0, 1]})
combs = it.product([bin(i) for i in range(2**H-1)], [bin(i) for i in range(2**W-1)])
count = 0
for comb in combs:
    rows = comb[0]
    cols = comb[1]
    rc_dict = {"row": [], "col": []}
    for j in range(H):
        if (int(rows, 0) >> j) & 1 == 1:
            rc_dict["row"].append(j)

    for j in range(W):
        if (int(cols, 0) >> j) & 1 == 1:
            rc_dict["col"].append(j)

    dat_c = plot(dat.copy(), rc_dict)
    if is_sat(dat_c):
        count += 1

print(count)






