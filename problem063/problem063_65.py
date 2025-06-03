import sys
import string
s = sys.stdin.read().lower()
for a in string.ascii_lowercase:
    print('{0} : {1}'.format(a, s.count(a)))