N = int(input())
ptn = [[0 for _ in range(10)] for __ in range(10)]
for num in range(1, N+1):
  str_num = str(num)
  if str_num[-1] != 0:
    ptn[int(str_num[0])][int(str_num[-1])] += 1
answer = 0
for i in range(10):
  for j in range(i, 10):
    if i == j:
      answer += ptn[i][j]**2
    else:
      answer += ptn[i][j]*ptn[j][i]*2
print(answer)