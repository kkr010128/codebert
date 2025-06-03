import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

a,b,c = MI()

if c < a+b:
    print('No')
else:
    print('Yes' if 4*a*b < (c-a-b)**2 else 'No')
