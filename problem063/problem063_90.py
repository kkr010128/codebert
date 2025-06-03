import sys
s = sys.stdin.read()
s = s.lower()
c = 97
while chr(c-1)!='z':
    print('{0} : {1}'.format(chr(c),s.count(chr(c))))
    c += 1

