import sys

line = sys.stdin.readline()
str_a, str_b = line.split(" ")
a = int(str_a)
b = int(str_b)

if a > b:
    c = ">"
elif a < b:
    c = "<"
else:
    c = "=="

print "a %s b" % (c)