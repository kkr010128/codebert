n = int(input())
lst = list(map(int,input().split()))
lst2 = [0 for i in range(n)]
for i in range(n - 1):
  x = lst[i]
  lst2[x - 1] = lst2[x - 1] + 1
for i in range(n):
  print(lst2[i])
