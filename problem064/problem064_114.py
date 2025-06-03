#!usr/bin/env python3

import sys
import re


def main():
    s = sys.stdin.readline()  # haystack
    p = sys.stdin.readline()  # needle

    s = s.strip('\n') * 2
    p = p.strip('\n')

    if len(re.findall((p), s)) > 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()