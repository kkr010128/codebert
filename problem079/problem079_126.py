from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under


s= int(input())
box_max =s//3
ans =0
if box_max ==0:
  print(ans)
else:
  for i in range(1, box_max +1):
     ball_and_bar =(s-3*i)+i-1
     bar =i-1
     ans += cmb(ball_and_bar, bar)%(10**9 +7)
  print(ans%(10**9 + 7))