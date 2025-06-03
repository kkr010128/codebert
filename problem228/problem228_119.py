n = int(input())


def saiki(i):
    if i > 1:
        return 2 * saiki(i // 2) + 1
    if i == 1:
        return 1


print(saiki(n))
