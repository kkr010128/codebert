n,m=map(int,input().split())
k=0
if n%2==1:
  for i in range(m):
    print(i+1,end=" ")
    print(n-i)
elif n%4==0:
  for i in range((n+2)//4):
    if k>=m:
      break
    print(i+1,end=" ")
    print(n-i)
    k+=1
  for i in range((n+2)//4,n//2):
    if k>=m:
      break
    print(i+1,end=" ")
    print(n-i-1)
    k+=1
else:
  for i in range((n+2)//4-1):
    if k>=m:
      break
    print(i+1,end=" ")
    print(n-i)
    k+=1
  for i in range((n+2)//4-1,n//2):
    if k>=m:
      break
    print(i+1,end=" ")
    print(n-i-1)
    k+=1