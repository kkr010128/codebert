# -*- coding: utf-8 -*-


def converter(a, b):
    larger = max(a, b)
    smaller = min(a, b)
    if larger == 0 or smaller == 0:
        return larger
    else:
        return converter(smaller, larger % smaller)        


def main():
    a, b = [int(x) for x in raw_input().strip().split(' ')]
    print converter(a, b) 


if __name__ == '__main__':
    main()