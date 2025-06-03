n, m = map(int, input().split())
L = list(map(int, input().split()))
a = 0
for i in range(len(L)):
  a = a + L[i] 
a = a / (4*m) 
nL = sorted(L, reverse=True)
if a <= nL[m-1]:
  print("Yes")
else:
  print("No")