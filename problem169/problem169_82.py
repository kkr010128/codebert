n = int(input())
lst = [int(i) for i in input().split()]

ans = [0] * n
for i in range(n-1):
  number = lst[i]
  ans[number - 1] += 1

for i in ans:
  print(i)