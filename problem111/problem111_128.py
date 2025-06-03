import sys

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')

def solve():
    n = ni()
    a = sorted(nl(), reverse=True)
    print(sum(a[:n//2]) + sum(a[1:(n+1)//2]))
    return

solve()
