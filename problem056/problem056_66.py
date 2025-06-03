n, m = map(int, input().split())

m2 = m

A = [list(map(int,input().split())) for i in range(n)]

b=[]
while m2 > 0:
  b_data = int(input())
  b.append(b_data)
  m2 = m2-1

  
for i in range(0,n):
  c = 0
  for j in range(0,m):
    c = c + (A[i][j] * b[j])
  print(c)
