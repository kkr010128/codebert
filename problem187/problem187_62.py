N ,X, Y = map(int, input().split()) 

rlt = [0]*N

for i in range(1,N+1):
  for j in range(i+1,N+1):
    if (i < X and j < X) or (i > Y and j > Y):
      rlt[j-i] += 1
    elif i < X and j > Y:
      rlt[X-i+j-Y+1] += 1
    elif i < X and j <= Y:
      rlt[min(j-i,X-i+1+Y-j)] += 1
    elif i >= X and j > Y:
      rlt[min(j-i,i-X+1+j-Y)] += 1
    elif i >= X and j <= Y:
      rlt[min(j-i,i-X+Y-j+1)] += 1
      
for i in rlt[1:]:
  print(i)