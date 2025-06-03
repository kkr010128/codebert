N = int(input())
cnt = 0
for a in range(1,N+1):
  b = N // a
  if a * b == N:
    cnt = cnt + b - 1
  else:
    cnt = cnt + b
print(cnt)