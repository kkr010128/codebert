import sys

alpha = 'abcdefghijklmnopqrstuvwxyz'
m = {k:0 for k in alpha}
q = ''
for line in sys.stdin:
    q += line

for s in q:
    s = s.lower()
    if s in m:
        m[s] += 1
    
for s in alpha:
    print('%s : %d' % (s, m[s]))