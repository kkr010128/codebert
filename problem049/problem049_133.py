# -*- coding: utf-8 -*-

while True:
    line = map(str, raw_input().split())
    H = int(line[0])
    W = int(line[1])
    if H+W:
        for i in range(H):
            print "#"*W
        print ""
    else:
        break