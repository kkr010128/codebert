n,m = map(int, input().split())
A = list(map(int,input().split()))

min_limit = sum(A)*(1 / (4*m))
select_ok = 0

for i in A:
  if i >= min_limit:
    select_ok += 1

if select_ok >= m:
  print("Yes")
else:
  print("No")
