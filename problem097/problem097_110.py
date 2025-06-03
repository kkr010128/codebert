n = int(input())

x = 7
ans = 1

#print(7%1)

for i in range(3*n):
  if x%n==0:
    break
  ans+=1
  x= x*10 + 7
  x=x%n
    
if ans < 3*n:
  print(ans)
else:
  print(-1)