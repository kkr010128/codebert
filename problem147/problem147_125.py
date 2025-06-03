import sys
S=sys.stdin.readline().strip()
T=sys.stdin.readline().strip()
if S==T[:-1]:
    print "Yes"
else:
    print "No"
