import sys

for line in sys.stdin:
    if len(line)>1:
        x1, y1, x2, y2 = line.strip('\n').split()
        x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
        print ((x1-x2)**2+(y1-y2)**2)**0.5