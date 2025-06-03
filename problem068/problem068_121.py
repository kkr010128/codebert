#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
???????????????
"""
inputstr = input().strip()
cmdnum = int(input().strip())

for i in range(cmdnum) :
    cmd = input().strip().split()

    if cmd[0] == "print":
        start = int(cmd[1])
        end = int(cmd[2]) + 1
        print(inputstr[start:end])

    if cmd[0] == "reverse":
        start = int(cmd[1])
        end = int(cmd[2]) + 1
        prev = inputstr[:start]
        revr = inputstr[start:end]
        next = inputstr[end:]
        inputstr = prev + revr[::-1] + next

    if cmd[0] == "replace":
        start = int(cmd[1])
        end = int(cmd[2]) + 1
        inputstr = inputstr[:start] + cmd[3] + inputstr[end:]