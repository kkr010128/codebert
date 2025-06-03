N = int(input())

memo = [[0]*10 for _ in range(10)]

for i in range(1,N+1):
  s = str(i)
  memo[int(s[0])][int(s[-1])] += 1
  
rlt = 0
for i in range(1,10):
  for j in range(1,10):
    rlt += memo[i][j]*memo[j][i]
    
print(rlt)