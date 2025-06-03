lst = []
num = int(input())
while num != 0:
  lst.append(num)
  num = int(input())

it = zip(range(len(lst)), lst)
for (c, v) in it:
  print("Case " + str(c+1) + ": " + str(v))