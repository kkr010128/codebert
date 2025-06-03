n,x,y = map(int,input().split())
k = [0]*(n)

for i in range(1,n):
  for j in range(i+1,n+1):
    if i < x and j <= x:
      k[j-i] += 1
    elif i >= y and j > y:
      k[j-i] += 1
    elif x <= i < y and x< j <= y:
      ind = min(j-i,i-x+y-j+1)
      k[ind] += 1
    elif i < x and x < j <= y:
      ind = min(j-i,x-i+y-j+1)
      k[ind] += 1
    elif x <= i < y and y < j:
      ind = min(j-i,i-x+1+j-y)
      k[ind] += 1
    elif i< x and j > y:
      ind = x - i + 1 + j - y
      k[ind] += 1
      
for i in range(1,n):
  print(k[i])