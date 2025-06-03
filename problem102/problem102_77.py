# coding: utf-8
import sys
from math import log


def change_into_int(lists):
    tmps = lists.split(' ')
    num_list = []
    for n in tmps:
        num_list.append(int(n))
    return num_list


if __name__ == "__main__":
    lines = []
    result_list = []
    # 入力
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    # int
    num1 = change_into_int(lines[0])
    data = change_into_int(lines[1])
    i = 0
    while(True):
        ans = data[i] - data[i+num1[1]]
        if ans < 0:
            print("Yes")
        else:
            print("No") 
        i = i + 1
        if i+num1[1] == len(data):
            break

