X = int(input())

count = 0
save = 100

while save < X:
  save += save // 100
  count += 1
  
print(count)