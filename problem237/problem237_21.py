import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
n = int(readline())
m = map(int,read().split())
xl = zip(m,m)
c = [(x-l,x+l) for x,l in xl]
  
from operator import itemgetter
c.sort()
c.sort(key=itemgetter(1))

ans = 1
chk = c[0][1]
for i,j in c:
  if i >= chk:
    ans +=1
    chk = j
    
print(ans)