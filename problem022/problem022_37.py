# -*- coding: utf-8 -*-


def main():
    s_length = int(raw_input())
    s = [int(x) for x in raw_input().strip().split(' ')]
    t_length = int(raw_input())
    t = [int(x) for x in raw_input().strip().split(' ')]

    counter = 0
    for value in t:
        if value in s:
            counter += 1

    print counter 

if __name__ == '__main__':
    main()