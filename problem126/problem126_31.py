x = list(map(int, input().split()))
count = 1
for i in x:
  if i == 0:
    print(count)
    break
  count += 1