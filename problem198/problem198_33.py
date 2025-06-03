#!/usr/bin python3
# -*- coding: utf-8 -*-

def stds(n):
    if n == 1:
        return set(['a'])
    else:
        std = stds(n-1)
        ret = set([])
        for stdi in std:
            for x in range(ord('a'),max(map(ord,list(stdi))) + 2):
                ret.add(stdi + chr(x))
        return ret

def main():
    N = int(input())
    ret = list(stds(N))
    ret.sort()
    print('\n'.join(ret))


if __name__ == '__main__':
    main()