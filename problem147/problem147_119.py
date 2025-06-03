import sys
a, b = (s.strip() for s in sys.stdin)
print('Yes' if a == b[:-1] else 'No')