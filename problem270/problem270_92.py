#!/usr/bin/env python3
s = input()
l = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
if s == 'SUN':
    print(7)
else:
    print(6 - l.index(s))