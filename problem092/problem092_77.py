# walking takahashi

def walk(X, K, D):
  abX = abs(X)
  if abX >= K*D:
    return abX - K*D
  itr = round(abX/D)
  ret = K - itr
  res = abs(abX - D*itr)
  if (ret % 2) == 0:
    return res
  return abs(res - D)

if __name__ == "__main__":
  inputs = list(map(int, input().split()))
  print(walk(inputs[0], inputs[1], inputs[2]))
