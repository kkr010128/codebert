#Macで実行する時
import sys
import os
if sys.platform=="darwin":
	base = os.path.dirname(os.path.abspath(__file__))
	name = os.path.normpath(os.path.join(base, '../atcoder/input.txt'))
	#print(name)
	sys.stdin = open(name)

a, b = map(int,input().split())

c = int(a/b)

if a%b!=0:
    c+=1

print(c)

