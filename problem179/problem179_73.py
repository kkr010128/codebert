# B Popular Vote

N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse = True)
border = sum(A) / (4 * M) 
cnt = 0
for a in A:
  if a >= border:
    cnt += 1
  else:
    break

if cnt >= M:
  print("Yes")
else:
  print("No")
