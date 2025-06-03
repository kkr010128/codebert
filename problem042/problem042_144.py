import sys
for i, x in enumerate(iter(sys.stdin.readline, '0\n'), 1):
    print(f'Case {i}: {x[:-1]}')
