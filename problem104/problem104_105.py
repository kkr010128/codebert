import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
L,R,d= map(int, readline().split())

print(R//d-(L-1)//d)