N = int(input())
res = 0

for j in range(1, N+1):
  div_num = N//j
  res += (div_num +1) * div_num * j // 2
print(res)