import sys

line = sys.stdin.readline()

a, b =line.split(" ")

a = int(a)
b = int(b)

if a < b:
    print "a < b"
elif a > b:
    print "a > b"
else:
    print "a == b"