#coding:utf-8
#1_8_D 2015.4.9
import re
s = input()
p = input()

if re.search(p , s * 2):
    print('Yes')
else:
    print('No')