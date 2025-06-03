import sys

inlist = list(map(int, sys.stdin.readline().split(" ")))

a = inlist[0]
b = inlist[1]

print("{0} {1} {2:f}".format(a // b, a % b, a / b))