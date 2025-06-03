import sys

a,b,c = map(int, sys.stdin.readline().rstrip().split(' '))
print('Yes' if (a<b<c) else 'No')