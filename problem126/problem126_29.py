n = [int(x) for x in input().split()]
for i in range(len(n)):
  if n[i] == 0:
    print(i + 1)
    break