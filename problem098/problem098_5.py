n = int(input())
lst = list(input())
r = lst.count('R')

count = 0

for i in range(0, r):
  if lst[i] == 'R':
    count += 1
    
print(r-count)