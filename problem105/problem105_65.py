import sys
readline = sys.stdin.readline

N = int(readline())
ans = 0
for a in list(map(int,readline().split()))[::2]:
  ans += (a & 1)
  
print(ans)