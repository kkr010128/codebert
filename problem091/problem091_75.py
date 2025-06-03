n = int(input())
line = input().split()

length = [int(line[i]) for i in range(n)]
length.sort(reverse = True)

count = 0

for i in range(n-2):
  long = length[i]
  
  for j in range(i+1,n-1):
    middle = length[j]
    if middle == long:
      continue
    if middle*2 <= long :
      break
      
    for k in range(j+1,n):
      short = length[k]
      if short == middle:
        continue
      if short + middle > long:
        count += 1
      else:
        break

print(count)