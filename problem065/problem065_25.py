# -*- coding: utf-8 -*-

import sys

w = sys.stdin.readline().strip()
count = 0

while True:
    t = list(map(str, input().split()))

    if 'END_OF_TEXT' in t:
        break

    for i in range(len(t)):
        if t[i].lower() == w:
            count += 1

print(count)

