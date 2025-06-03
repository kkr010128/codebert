import sys
lines = sys.stdin.readlines()
l = map(int, lines[1].split())
print min(l),max(l),sum(l)