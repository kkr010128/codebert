N= int(input())
a = [0]*110000
if N == 2:
  print(2)
else:
  for i in range(2,N):
    k = i
    j = 2
    while k<110000:
      a[k]+=1
      k = int((k/(j-1))*j)
      j+=1
  
  for i in range(N,110001):
    if a[i]>0:
      continue
    elif a[i]==0:
      print(i)
      break