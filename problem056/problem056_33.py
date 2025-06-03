import sys

(row, column) = sys.stdin.readline().rstrip('\r\n').split(' ')
row = int(row)
column = int(column)

a = []
b = []
c = []

for ii in range(row):
  a.append([int(x) for x in input().rstrip('\r\n').split(' ')])

for ii in range(column):
  b.append(int(input().rstrip('\r\n')))

for ii in range(len(a)):
  work = 0
  for jj in range(len(a[ii])):
    work += a[ii][jj] * b[jj]
  c.append(work)

for cc in c:
  print(cc)

