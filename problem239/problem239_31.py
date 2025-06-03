#Macで実行する時
import sys
import os
if sys.platform=="darwin":
	base = os.path.dirname(os.path.abspath(__file__))
	name = os.path.normpath(os.path.join(base, '../atcoder/input.txt'))
	#print(name)
	sys.stdin = open(name)

a = str(input())

print(chr(ord(a)+1))


