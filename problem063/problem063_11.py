import sys

s = ''
for line in sys.stdin:
    s += line
s = s.lower()
count = {letter: s.count(letter) for letter in set(s)}
for c in range(97,97+26):
    if chr(c) in count:
        print("%c : %d" % (chr(c), count[chr(c)]))
    else:
        print("%c : 0" % chr(c))