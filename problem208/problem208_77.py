n, m = [int(i) for i in input().split()]
n_list = [10] * n
for _ in range(m):
  si, ci = [int(i) for i in input().split()]
  if n_list[si - 1] == 10:
    n_list[si - 1] = ci
  elif n_list[si - 1] != ci:
    print(-1)
    exit()
if n != 1:
  ans = n_list[0] if n_list[0] != 10 else 1
else:
  ans = n_list[0] if n_list[0] != 10 else 0
if ans == 0 and n != 1:
  print(-1)
  exit()
for ai in n_list[1:]:
  if ai != 10:
    ans = ans * 10 + ai
  else:
    ans = ans * 10
print(ans)