N, X, T = map(int, input().split())
times = N // X
if N % X != 0:
  times += 1
print(T * times)
