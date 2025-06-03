n, m, k = map(int, input().split())
a_books = [int(i) for i in input().split()]
b_books = [int(i) for i in input().split()]

time = 0
count = 0
for i in range(n):
  time += a_books[i]
  if time > k:
    time -= a_books[i]
    i -= 1
    break
  count += 1
for j in range(m):
  time += b_books[j]
  if time > k:
    time -= b_books[j]
    j -= 1
    break
  count += 1
max_count = count
#print(max_count, time)
while j < m and i >= 0:
  time -= a_books[i]
  i -= 1
  count -= 1
  j += 1
  while j < m:
    time += b_books[j]
    if time > k:
      time -= b_books[j]
      j -= 1
      break
    count += 1
    j += 1
  if count > max_count:
    max_count = count
  #print(count, time)
  #print(max_count)
print(max_count)