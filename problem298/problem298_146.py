x = list(map(int, input().split()))
h = list(map(int, input().split()))
count = 0
for i in h:
  if x[1] <= i:
    count += 1
print(count)