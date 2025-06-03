import sys

lines = [line.strip() for line in sys.stdin]
s = lines[0] + lines[0]
p = lines[1].strip()

if s.find(p) != -1:
    print('Yes')
else:
    print('No')