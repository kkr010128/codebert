first_line = raw_input().split(" ")
n = int(first_line[0])
m = int(first_line[1])
l = int(first_line[2])

array_a = []
array_b = []
for i in xrange(n):
  line = map(int, raw_input().split(" "))
  array_a.append(line)
for i in xrange(m):
  line = map(int, raw_input().split(" "))
  array_b.append(line)

# print array_a
# print array_b

array_c = []
for i in xrange(n):
  line = []
  for j in xrange(l):
    sum = 0
    for k in xrange(m):
      sum += array_a[i][k] * array_b[k][j]
    line.append(sum)
  array_c.append(line)

for i in xrange(n):
  print " ".join(map(str, array_c[i]))