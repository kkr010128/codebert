# encoding: utf-8


import sys

__input = sys.stdin.readlines()
length_1 = int(__input[0])
array_1 = list(map(int, __input[1].split()))
length_2 = int(__input[2])
array_2 = list(map(int, __input[3].split()))

record = [False] * 2000


def solution():
    # print(length_1, array_1, length_2, array_2)
    assert length_1 == len(array_1) and length_2 == len(array_2)

    for i in array_1:
        # record[i] = True
        for j in range(2000 - i, 0, -1):
            if record[j]:
                # print(j, i + j)
                record[i + j] = True
        record[i] = True

    for index in array_2:
        if record[index]:
            print("yes")
        else:
            print("no")


if __name__ == '__main__':
    solution()