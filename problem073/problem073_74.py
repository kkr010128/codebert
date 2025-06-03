# -*- coding: utf-8 -*-

def input_int():
    return int(input())


def answer():
    n = input_int()

    count = 0
    for a in range(1, n):
        b = (n - 1) // a
        if b >= a:
            count += (b - a) * 2
            count += 1
        else:
            continue
    print(count)


answer()