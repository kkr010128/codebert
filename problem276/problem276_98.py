N = int(input())
A = list(map(int, input().split()))
s = sum(A)

av = s / 2
x = 0
y = 0

for i in range(N):
  x += A[i]
  
  if x < av < x +A[i+1]:
    
    y = s - x - A[i+1]
    
    if x > y:
      print(A[i+1]-x+y)
      
    else:
      print(A[i+1]-y+x)
  elif x == av:
    print(0)