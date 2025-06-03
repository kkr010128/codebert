N = int(input())
array = [0]*N
for i in range(N):
  if (i+1) % 3 == 0 or (i+1) % 5 == 0:
    continue
  else:
    array[i] = i+1
print( sum(array) )
