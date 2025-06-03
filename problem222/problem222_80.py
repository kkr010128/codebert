#import math
import collections
#n,k = map(int, input().split( ))
#A = list(map(int, input().split( )))
n = int(input())
A = list(map(int, input().split( )))
c = collections.Counter(A)

a = c.most_common()[0][1]
if a != 1:
  print('NO')
else:
  print('YES')