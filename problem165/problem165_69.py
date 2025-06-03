import sys, itertools
print(len(set(itertools.islice(sys.stdin.buffer, 1, None))))