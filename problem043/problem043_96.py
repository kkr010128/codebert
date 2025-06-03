import sys
for e in iter(sys.stdin.readline, '0 0\n'):
    print(*sorted(map(int, e.split())))
