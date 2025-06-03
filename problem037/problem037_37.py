import sys
S = int(sys.stdin.readline())
h = int(S / 60 / 60)
m = int(S % 3600 / 60)
s = S % 60
print("%d:%d:%d" % (h, m, s))