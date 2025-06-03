N = int(input())
flag = 'No'
cnt = 0
for i in range(N):
  d1, d2 = map(int, input().split())
  if d1 == d2:
    cnt += 1
    if cnt == 3:
      flag = 'Yes'
  else:
    cnt = 0
print(flag)