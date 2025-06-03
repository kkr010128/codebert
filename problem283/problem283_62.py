N = int(input())
if N % 2 == 0:
  ans = (N / 2) - 1
else:
  ans = (N - 1) / 2
print(int(ans))