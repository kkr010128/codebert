#coding: utf-8
import sys
c = [0 for i in range(26)]
in_list = []

for line in sys.stdin:
    in_list.append(line)

for s in in_list:
    for i in range(len(s)):
        if   ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z'):
            c[ord(s[i])-97] += 1
        elif ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
            c[ord(s[i])-65] += 1

for i in range(26):
    print(chr(ord('a')+i) + " : " + str(c[i]))
