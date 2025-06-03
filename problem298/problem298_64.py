n,k = map(int, input().split())
ki = list(map(int,input().split()))
count = 0

for i in range(n):
  if ki[i] >= k:
    count += 1
  else:
    pass

print(count)