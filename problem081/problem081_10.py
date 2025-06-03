#!/usr/bin/env python

d, t, s = [int(i) for i in input().split(' ')]

if s*t >= d:
    print('Yes')
else:
    print('No')
