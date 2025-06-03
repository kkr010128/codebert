import sys
from collections import Counter

c = Counter()
for line in sys.stdin.readlines():
    c.update(line.lower())
for a in 'abcdefghijklmnopqrstuvwxyz':
    print a + ' :', c.get(a, 0)