k = int(input())
a = 7 % k
count = 1
for i in range(1,k+1):
  if a == 0:
    print(count)
    break
  else:
    a = (10 * a + 7) % k
    count += 1
    if i == k:
      print(-1)