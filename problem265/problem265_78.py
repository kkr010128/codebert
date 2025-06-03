N = int(input())
for i in range(1 , N + 1):
  x = int(i * 1.08)
  if x == N:
    print(i)
    exit()
print(':(')