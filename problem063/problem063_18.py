import sys
STRING = ""
for line in sys.stdin:
    STRING += line.lower()
CHRS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in CHRS:
    print("%s : %d" % (i, STRING.count(i)))