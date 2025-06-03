N,M = map(int,input().split())
array = list(map(int,input().split()))
total = sum(array)
count = 0
for i in range(N):
  if array[i] < total / (4*M) :
    continue
  else:
    count += 1
print('Yes' if count >= M else 'No')