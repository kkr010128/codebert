n = int(input())
squares = list(map(int, input().split(" ")))

odd = 0
for i in range(0, n, 2):
  if squares[i] % 2:
    odd += 1
print(odd)