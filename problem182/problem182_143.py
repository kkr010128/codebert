n,k,c = map(int,input().split())
s = list(input())

L = []
R = []

i = -1
j = n  

for ki in range(k):
  while i < n:
    i += 1
    if s[i] == 'o':           
      L += [i]
      i += c
      break

for ki in range(k):      
  while 0 <= j:
    j -= 1
    if s[j] == 'o':          
      R += [j]
      j -= c
      break
      
for i in range(k):
  if L[i] == R[-i-1] :
    print(L[i]+1)