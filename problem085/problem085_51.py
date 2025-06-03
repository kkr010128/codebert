N = int(input())
A = list(map(int, input().split()))
 
B = [0 for i in range(max(A)+1)]
 
for i in range(2, len(B)):
  if B[i] != 0:
    continue
  for j in range(i, len(B), i):
    B[j] = i

def func(X):
  buf = set()
  while X>1:
    x = B[X]
    buf.add(x)
    while X%x==0:
      X = X//x
  #print(buf)
  return buf
 
set1 = func(A[0])
set2 = func(A[0])
totallen = len(set1)
for a in A[1:]:
  set3 = func(a)
  totallen += len(set3)
  #print(a, set1, set2)
  set1 |= set3
  set2 &= set3
  #print(set1, set2, set3)
#print(totallen, set1, set2)
if len(set2)!=0:
  print("not coprime")
elif len(set1)==totallen:
  print("pairwise coprime")
else:
  print("setwise coprime")