import sys

x = sys.stdin.readline()

a, b = x.split(" ")

a = int(a)
b = int(b)

S = a * b
l = 2 * (a + b)

print '%d %d' % (S,l)