import sys

alpha = [chr(i) for i in range(97,97+26)]
line = ""

for l in sys.stdin:
    line += l.lower()
    
for i in alpha:
    print("{0} : {1}".format(i, line.count(i)))