[N, X, T] = list(map(int, input().split()))
#N個のたこ焼きを作るためにタコ焼き機を使う回数Y
if N % X == 0:
  Y = N // X
else:
  Y = N // X + 1

ans = T * Y
print(ans)