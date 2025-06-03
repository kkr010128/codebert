N = float(input())
S = N
count = 0
while (N > 0):
  if N % 2 != 0:
    count += 1
  N = N - 1
print(count / S)