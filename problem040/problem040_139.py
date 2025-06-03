import sys

list = map(int,sys.stdin.readline().split())
list.sort()
print(' '.join(map(str,list)))