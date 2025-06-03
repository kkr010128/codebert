# coding: utf-8
# 二分探索（応用）


def loading(pack_list, k, q):

    truck = 0
    idx = 0
    for pack in pack_list:
        if pack > q:
            return False

        if truck + pack > q:
            idx += 1
            truck = 0

        truck += pack

    if truck > 0:
        idx += 1

    return False if idx > k else True


if __name__ == "__main__":
    n, k = [int(i) for i in input().split()]

    pack = []

    for _ in range(n):
        pack.append(int(input()))

    min = 0
    max = int(1E20)
    # min = sum(pack) // n
    # max = sum(pack)

    q = (max + min) // 2

    res = loading(pack, k, q)

    while min + 1 != max:
        min, max = [min, q] if res else [q, max]
        q = (max + min) // 2

        res = loading(pack, k, q)

    print(max)

