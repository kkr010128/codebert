import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

n = readint()

ans = 0
for a in range(1,n):
    b = n//a
    if a*b==n:
        ans += b-1
    else:
        ans += b

print(ans)
    

