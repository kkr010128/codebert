#!usr/bin/env python3

import sys


def string_to_list_spliter():
    n = sys.stdin.readline()
    lst = [int(i) for i in sys.stdin.readline().split()]
    return lst


def main():
    lst = string_to_list_spliter()
    print(min(lst), max(lst), sum(lst))


if __name__ == '__main__':
    main()