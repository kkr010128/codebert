import sys
prm = sys.stdin.readline()
S = int(prm)
h = S / (60 * 60);
S = S % (60 * 60);
m = S / 60;
s = S % 60;
print str(h)+':'+str(m)+':'+str(s)