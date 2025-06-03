#!/usr/bin/env python3

n = list(input())

if '3' == n[-1]:
    print('bon')
elif n[-1] in ['0', '1', '6', '8']:
    print('pon')
else:
    print('hon')
