import sys

def selectionSort(x_list, y):
  a = 0
  for i in range(y):
    minj = i
    for j in range(i, y):
      if x_list[j] < x_list[minj]:
        minj = j
    x_list[i], x_list[minj] = x_list[minj], x_list[i]
    if x_list[i] != x_list[minj]:
      a += 1
  return a

y = sys.stdin.readline()
y = int(y)
 
x = sys.stdin.readline()
x_list = x.split(" ")
 
for i in range(y):
  x_list[i] = int(x_list[i])
 
a = selectionSort(x_list, y)
 
for k in range(0, y):
  print x_list[k],
print
print a