N = int(input())
count = 0
L = list(map(int, input().split()))
for i,li in enumerate(L[:-2]):
  for j,lj in enumerate(L[i+1:-1]):
    for k,lk in enumerate(L[i+j+1:]):
      if (li != lj) and (lj != lk) and (li != lk):
#        la,lb,lc = sorted([li,lj,lk])
        if li + lj > lk and lj + lk > li and lk + li > lj:
#          print(i+1,i+j+1,i+j+k+1,li,lj,lk)
          count += 1
print(count)