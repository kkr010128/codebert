n = int(input())
a = list(map(int,input().split()))
if 1 not in a:
  print(-1)
  exit()
num_break = 0
pos = 1

for i in a:
  if i == pos:
    pos += 1
  else:
    num_break += 1
print(num_break)