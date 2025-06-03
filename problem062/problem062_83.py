# coding: utf-8

import sys

ans = []
while ( 1 ):
    
    strings = input()
    if (len(strings) == 1 and int(strings[0]) == 0):
        break
    
    ans = 0
    for s in strings:
        ans += int(s)
    print(ans)