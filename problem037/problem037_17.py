import sys

line = sys.stdin.readline()
s = int(line) % 60
i = int(line) / 60
m = i % 60
h = i /60
print str(h) + ":" + str(m) + ":" + str(s)