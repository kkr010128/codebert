N=int(input())
n= str(N)
total=0
for i in range(len(n)):
  k = n[i]
  k = int(k)
  total += k
  
if total%9==0:
  print("Yes")
else:
  print("No")