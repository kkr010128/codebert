alphabet = 'abcdefghijklmnopqrstuvwxyz'
from collections import defaultdict
import sys

adict = defaultdict(int)

for l in sys.stdin:
    for c in l.lower():
        adict[c] += 1
        
for k in alphabet:
    print('%s : %i' %(k, adict[k]))