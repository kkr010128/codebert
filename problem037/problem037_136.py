import sys

line = sys.stdin.readline()
inp = int(line)

h,mod = inp//3600, inp%3600
m,mod = mod//60, mod%60
s = mod

print ("%d:%d:%d" % (h,m,s))