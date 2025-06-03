tmp = input()
line = input().split(" ")
for i in range(len(line)):
  line[i] = int(line[i])
line.sort()
count = 0
for i in range(0, len(line) - 2):
  for j in range(1, len(line) - 1):
    if i > j or i == j:
      continue
    for k in range(2, len(line)):
      if j > k or j == k:
        continue
      if int(line[i]) != int(line[j]) and int(line[j]) != int(line[k]):
        if int(line[i]) + int(line[j]) > int(line[k]):
          count += 1
print(count)