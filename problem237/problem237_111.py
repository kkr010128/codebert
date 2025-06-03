N=int(input())
import sys
l=[i.rstrip().split() for i in sys.stdin.readlines()]
l=[list(map(int,i)) for i in l]
l=[[i-j,i+j] for i,j in l]
from operator import itemgetter
l.sort(key=itemgetter(1))
ans=N
end=l[0][1]
for i in range(N-1):
   if l[i+1][0] < end:
      ans-=1
   else:
      end=l[i+1][1]
print(ans)