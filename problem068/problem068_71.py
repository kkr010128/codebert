# -*- coding: utf-8 -*-

import sys
import os


s = input().strip()
N = int(input())
for i in range(N):
    lst = input().split()
    command = lst[0]
    if command == 'replace':
        a = int(lst[1])
        b = int(lst[2])
        p = lst[3]
        s = s[:a] + p + s[b+1:]
    elif command == 'reverse':
        a = int(lst[1])
        b = int(lst[2])
        part = s[a:b+1]
        part = part[::-1]
        s = s[:a] + part + s[b+1:]
    elif command == 'print':
        a = int(lst[1])
        b = int(lst[2])
        print(s[a:b+1])
    else:
        print('error')
    #print('s', s)