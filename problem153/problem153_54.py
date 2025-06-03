import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = read().rstrip().decode()
x = ['ABC', 'ARC']
x.remove(S)
print(x[0])
