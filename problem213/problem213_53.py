def nearest_int(f):
  if f - int(f) < 0.5:
    return int(f)
  else:
    return int(f) + 1

N = int(input())
X = list(map(lambda x: int(x), input().split(" ")))
ave = sum(X) / N
avei = nearest_int(ave)

print(sum([(x - avei) ** 2 for x in X]))