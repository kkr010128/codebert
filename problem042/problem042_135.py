import sys
for i, x in enumerate(map(int, sys.stdin)):
    if not x: break
    print("Case {0}: {1}".format(i + 1, x))