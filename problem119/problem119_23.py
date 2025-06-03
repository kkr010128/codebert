#!/usr/bin/env python3


def next_line():
    return input()


def next_int():
    return int(input())


def next_int_array_one_line():
    return list(map(int, input().split()))


def next_int_array_multi_lines(size):
    return [int(input()) for _ in range(size)]


def next_str_array(size):
    return [input() for _ in range(size)]


def main():
    a = next_line()
    if 'A' <= a[0] and a[0] <= 'Z':
        print("A")
    else:
        print("a")


if __name__ == '__main__':
    main()
