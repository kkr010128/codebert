#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinput

if __name__ == '__main__':
    for line in fileinput.input():
        tokens = line.strip().split()
        a, b = int(tokens[0]), int(tokens[1])
        if a == b == 0:
            pass
        elif a <= b:
            print '%d %d' % (a, b)
        elif b < a:
            print '%d %d' % (b, a)