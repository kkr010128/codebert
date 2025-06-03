K = int(input())

C = [[0]*10 for _ in range(10)]
C[0] = [1]*10
D = {0: [0, 1], 1: [0, 1, 2], 2: [1, 2, 3], 3: [2, 3, 4], 4: [3, 4, 5], 5: [4, 5, 6], 6: [5, 6, 7], 7: [6, 7, 8], 8: [7, 8, 9], 9: [8, 9]}

for i in range(1, 10):
  for j in range(10):
    if j == 0:
      C[i][j] = C[i-1][j] + C[i-1][j+1]
    elif j == 9:
      C[i][j] = C[i-1][j-1] + C[i-1][j]
    else:
      C[i][j] = C[i-1][j-1] + C[i-1][j] + C[i-1][j+1]

ans = []
temp = K
Flag = True

for i in range(10):
  if Flag:
    for j in range(1, 10):
      temp -= C[i][j]
      if temp <= 0:
        temp += C[i][j]
        r = i
        ans.append(j)
        Flag = False
        break
  else:
    break

def f(x, r):
  temp = x
  r -= 1
  for j in D[ans[-1]]:
    temp -= C[r][j]
    if temp <= 0:
      temp += C[r][j]
      ans.append(j)
      break
  return temp, r

while r >= 1:
  temp, r = f(temp, r)

print("".join([str(i) for i in ans]))