import sys
a = [0]*26
s = sys.stdin.read().lower()
for i in map(chr, range(ord('a'), ord('z')+1)):
    print(i, ':', s.count(i))

