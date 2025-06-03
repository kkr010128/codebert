import sys

for index, line in enumerate(sys.stdin):
    value = int(line.strip())
    if value == 0:
        break
    print("Case {0}: {1}".format(index+1, value))