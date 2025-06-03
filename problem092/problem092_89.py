X, K, D = map(int, input().split())

t = X // D
if abs(t) >= K:
  if X > 0:
  	print(abs(X-(D*K)))
  elif X < 0:
    print(abs(X+(D*K)))
  exit(0)

nokori = K - t
if X-(D*t) <= 0:
  if nokori % 2 == 0:
  	print(abs(X-(D*t)))
  else:
    print(abs(X-(D*(t-1))))
else:
  if nokori % 2 == 0:
  	print(abs(X-(D*t)))
  else:
    print(abs(X-(D*(t+1))))
