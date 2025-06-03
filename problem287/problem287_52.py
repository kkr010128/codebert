N = int(input())

# A*B=Nとなるような1以上9以下の整数(A, B)が存在するかどうか全探索を行う
ans = 'No'
for i in range(1, 10):
  for j in range(1, 10):
    if i*j == N:
      ans = 'Yes'
      break
      
print(ans)