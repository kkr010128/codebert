n = int(input())

aaa = [[0 for i in range(10)] for j in range(10)]

for i in range(1, n+1):
  aaa[int(str(i)[0])][i%10] += 1

ans = 0
for i in range(1, 10):
  for j in range(1, 10):
    ans += aaa[i][j]*aaa[j][i]
print(ans)