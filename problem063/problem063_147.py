import sys
import string

s = sys.stdin.read().lower()
for c in string.ascii_lowercase:
    print(c, ":", s.count(c))