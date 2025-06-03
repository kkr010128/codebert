import sys
l = [int(i) for i in sys.stdin.readline().split()]
l.sort()
print(" ".join(map(str, l)))