import sys
for line in sys.stdin:
    if line.find("?") != -1:
        break
    print(int(eval(line)))