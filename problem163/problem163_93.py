import sys
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
S,W = map(int, readline().split())
 
 
if S > W:
  print('safe')
else:
  print('unsafe')