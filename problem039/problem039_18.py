#!/usr/bin/env python

if __name__=='__main__':
    a, b, c = map(int, raw_input().split())
    print 'Yes' if a < b and b < c else 'No'

