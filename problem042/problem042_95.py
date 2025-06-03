import sys

i = 1
for line in sys.stdin.readlines():
    x = line.strip()
    if x != "0":
        print("Case {}: {}".format(i, x))
    i += 1