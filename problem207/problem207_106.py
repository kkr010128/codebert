import numpy as np
a1 = [int(x.strip()) for x in input().split()]
a2 = [int(x.strip()) for x in input().split()]
a3 = [int(x.strip()) for x in input().split()]
a = np.array([a1,a2,a3])
n = int(input())
bingo = 0
for i in range(n):
  b = int(input())
  if b in a:
    ch = np.argwhere(a==b)
    a[ch[0][0]][ch[0][1]] = 0 #該当する文字をゼロでパンチング
sum_col = np.sum(a, axis=0)
sum_row = np.sum(a, axis=1)
bingo = np.count_nonzero(sum_col==0) + np.count_nonzero(sum_row==0)
if a[0,0]==0 and a[1,1]==0 and a[2,2]==0:
  bingo += 1
if a[2,0]==0 and a[1,1]==0 and a[0,2]==0:
  bingo += 1
if bingo > 0:
  ans = 'Yes'
else:
  ans = 'No'
print(ans)