#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

in_str = sys.stdin.readline().strip()
q = int(sys.stdin.readline())

for i in range(q):
    command = sys.stdin.readline().split()
    pos_a = int(command[1])
    pos_b = int(command[2])

    if command[0] == 'print':
        print(in_str[pos_a:pos_b+1])
    elif command[0] == 'reverse':
        if pos_a == 0: to_pos = None
        else: to_pos = pos_a - 1
        in_str = in_str[:pos_a] + in_str[pos_b:to_pos:-1] + in_str[pos_b+1:]
    elif command[0] == 'replace':
        in_str = in_str[:pos_a] + command[3] + in_str[pos_b+1:]
    else:
        raise ValueError

