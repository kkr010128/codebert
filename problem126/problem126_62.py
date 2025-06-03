lst = [int(i) for i in input().split()]

for i in range(5):
  if lst[i] == 0:
    print(i + 1)
    break