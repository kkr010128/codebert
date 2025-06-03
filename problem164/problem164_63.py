A, B, C, D = map(int, input().split())

while True:
  C -= B
  if C <= 0: break
  A -= D
  if A <= 0: break
  
if C <= 0: print('Yes')
elif A <= 0: print('No')