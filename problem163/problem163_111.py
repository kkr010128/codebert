import sys

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prl = lambda x: print(*x ,sep='\n')

s,w = nm()
print('unsafe' if s <= w else 'safe')