import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A,B = map(int, read().split())
temp = [A,B]
 
for i in range(1,4):
  if i not in temp:
    print(i)