import sys
uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowers = 'abcdefghijklmnopqrstuvwxyz'
s = []
for line in sys.stdin:
    s += line
for i in range(26):
    print(lowers[i] + ' : ' + str(s.count(uppers[i]) + s.count(lowers[i])))