N = int(input())
A = list(map(int, input().split())) 

manzoku = 1
hakai = 0

for i in range(N):
  if A[i] == manzoku:
    manzoku += 1
  else:
    hakai += 1

if hakai == N: 
  print(-1)
else:
  print(hakai)