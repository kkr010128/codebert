a = int(input())
b = int(input())
l = [a,b]

for i in range(1,4):
  if i not in l:
    print(i)
    exit()