import sys

data = sys.stdin.readline().strip().split(' ')
a = int(data[0])
b = int(data[1])

print('%d %d %.5f' % (a // b, a % b, a / b))