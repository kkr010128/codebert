import sys
prm = sys.stdin.readline()
prm = prm.split()
a = int(prm[0])
b = int(prm[1])
c = int(prm[2])

if a < b and b < c :
    print 'Yes'
else :
    print 'No'