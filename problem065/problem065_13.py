# -*- coding: utf-8 -*-

import sys

word = str(raw_input())
count = 0;

while True:
    line = map(str, raw_input().split())
    for i in line:
        if i == "END_OF_TEXT":
            print count
            sys.exit()
        if i.lower() == word:
            count += 1