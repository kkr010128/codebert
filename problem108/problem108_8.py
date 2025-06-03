n = int(input())
for i in range(11):
  if 1000*i >= n:
    print(1000*i - n)
    exit()
