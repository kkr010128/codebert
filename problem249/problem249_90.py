A,B,K = map(int,input().split())
if K>A+B:
  A,B = 0,0
elif K>A:
  A,B = 0,B-K+A
else:
  A -= K
print(f'{A} {B}')