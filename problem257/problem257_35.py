_ = input()
A = [int(i) for i in input().split()]

cnt = 1
broken = 0
for a in A:
  if a == cnt:
    cnt += 1
  else:
    broken += 1

if cnt == 1:
  print("-1")
else:
  print(broken)