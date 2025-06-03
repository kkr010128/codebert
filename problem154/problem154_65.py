n, k = map(int, input().split())
check = [False] * n
d = []
a = []
for i in range(k):
  d = int(input())
  a.append(list(map(int, input().split())))
for i in range(k):
  for j in range(len(a[i])):
    check[a[i][j]-1] = True
print(check.count(False))