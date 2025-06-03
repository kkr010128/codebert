import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))


n,a,b = readints()

if (b-a)%2==0:
    print((b-a)//2)
else:
    print(min(n-b+(b-a)//2+1,a-1+(b-a)//2+1))



