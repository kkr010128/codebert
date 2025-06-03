n,m = map(int, input().split())
H_list = list(map(int, input().split()))
line = [1 for i in range(n)]
for i in range(m):
  a,b = map(int, input().split())
  if H_list[a-1] < H_list[b-1]:
    line[a-1] = 0
  elif H_list[a-1] > H_list[b-1]:
    line[b-1] = 0
  else:
    line[a-1] = 0
    line[b-1] = 0
print(sum(line))