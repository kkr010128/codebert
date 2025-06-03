n = int(input())
d = [list(map(int,input().split())) for i in range(n)]
count = 0

# [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]

for i in d:
  if i[0] == i[1]:
    count += 1
  else:
    count = 0
  if count == 3:
    print('Yes')
    exit()
print('No')