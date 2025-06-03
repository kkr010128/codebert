#Macで実行する時
import sys
import os
if sys.platform=="darwin":
	base = os.path.dirname(os.path.abspath(__file__))
	name = os.path.normpath(os.path.join(base, '../atcoder/input.txt'))
	sys.stdin = open(name)

s = input()

if s[2]==s[3] and s[4]==s[5]:
    print("Yes")
else:
    print("No")


